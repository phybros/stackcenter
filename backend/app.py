import base64
import subprocess
import uuid

import docker
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import Stack

LABEL_COM_DOCKER_COMPOSE_PROJECT = 'com.docker.compose.project'

stackcenterapp = Flask(__name__)
CORS(stackcenterapp)

stackcenterapp.config['DEBUG'] = True
stackcenterapp.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
stackcenterapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(stackcenterapp)
migrate = Migrate(stackcenterapp, db)

db.init_app(stackcenterapp)

with stackcenterapp.app_context():
    from flask_migrate import upgrade as _upgrade
    _upgrade(directory='migrations')

# @app.before_first_request
# def before_first_request():
# db.create_all()
# client = docker.from_env()
#
# for container in client.containers.list():
#     for label, v in container.labels.items():
#         if label == LABEL_COM_DOCKER_COMPOSE_PROJECT:
#             stacks[v] = ""

# pass


@stackcenterapp.route('/', methods=['GET'])
def root():
    return stackcenterapp.send_static_file('index.html')


@stackcenterapp.route('/js/<path:path>', methods=['GET', 'OPTIONS'])
def servejs(path):
    return stackcenterapp.send_static_file('js/{}'.format(path))


@stackcenterapp.route('/css/<path:path>', methods=['GET', 'OPTIONS'])
def servecss(path):
    return stackcenterapp.send_static_file('css/{}'.format(path))


@stackcenterapp.route('/api/stacks', methods=['POST'])
def create_stack():
    new_id = str(uuid.uuid4())
    posted = request.json
    decoded = base64.b64decode(posted['composeYml']).decode('utf-8')

    newstack = Stack(id=new_id, name=str(posted['name'].lower()), compose_yml=posted['composeYml'])
    db.session.add(newstack)
    db.session.commit()

    # run docker compose
    results = subprocess.run(
        [
            'docker-compose',
            '-p',
            str(posted['name'].lower()),
            '-f',
            '-',
            'up',
            '-d'
        ],
        input=bytes(decoded, encoding='utf-8'),
        capture_output=True)

    # docker compose status goes on stderr?
    return jsonify({'result': str(results.stderr)})


@stackcenterapp.route('/api/stacks', methods=['GET', 'OPTIONS'])
def all_stacks():
    client = docker.from_env()
    stacks = Stack.query.all()

    result = []
    external_stack_names = []

    for container in client.containers.list():
        for label, v in container.labels.items():
            if label == LABEL_COM_DOCKER_COMPOSE_PROJECT:
                if v not in external_stack_names:
                    external_stack_names.append(v)

    for stack in stacks:
        result.append({
            'Id': stack.id,
            'Name': stack.name,
            'Config': stack.compose_yml,
        })

    for es in external_stack_names:
        if not name_in_array(es, result):
            result.append({
                'Id': 'external:' + es,
                'Name': es,
                'Config': None,
            })

    return jsonify(result)


def name_in_array(name, arr):
    for a in arr:
        if 'Name' in a and a['Name'] == name:
            return True

    return False


@stackcenterapp.route('/api/stacks/<stack_id>', methods=['GET', 'OPTIONS'])
def stack_by_id(stack_id):
    stack = Stack.query.filter_by(id=stack_id).first()

    return jsonify({
        'Id': stack.id,
        'Name': stack.name,
        'Config': stack.compose_yml,
    })


@stackcenterapp.route('/api/images', methods=['GET', 'OPTIONS'])
def all_images():
    client = docker.from_env()

    for image in client.images.list(all=True):
        print(image.attrs)


@stackcenterapp.route('/api/containers', methods=['GET', 'OPTIONS'])
def all_containers():
    client = docker.from_env()

    response = []
    for container in client.containers.list(all=True):
        custom_stuff = {
            'Stack': '',
        }

        # Figure out the stack name
        for label, v in container.labels.items():
            if label == LABEL_COM_DOCKER_COMPOSE_PROJECT:
                custom_stuff['Stack'] = v

        name = {
            'Name': container.name.lstrip('/')
        }

        response.append(
            {**container.attrs, **{'StackCenter': custom_stuff}, **name})

    return jsonify(response)


@stackcenterapp.route('/api/containers/<container_id>', methods=['GET', 'OPTIONS'])
def one_container(container_id):
    client = docker.from_env()

    custom_stuff = {
        'Stack': ''
    }

    container = client.containers.get(container_id)

    # Figure out the stack name
    for label, v in container.labels.items():
        if label == LABEL_COM_DOCKER_COMPOSE_PROJECT:
            custom_stuff['Stack'] = v

    return jsonify({**container.attrs, **{'StackCenter': custom_stuff}})


@stackcenterapp.route('/api/stacks/<stack_id>/containers', methods=['GET'])
def containers_in_stack(stack_id):
    stack = Stack.query.filter_by(id=stack_id).first()
    client = docker.from_env()

    custom_stuff = {
        'Stack': '',
    }

    result = []
    for container in client.containers.list():
        for label, v in container.labels.items():
            if label == LABEL_COM_DOCKER_COMPOSE_PROJECT:
                if v == stack.name:
                    result.append({**container.attrs, **{'StackCenter': {'Stack': v}}, **{'Name': container.name.lstrip("/")}})

    return jsonify(result)


@stackcenterapp.route('/api/networks', methods=['GET', 'OPTIONS'])
def all_networks():
    client = docker.from_env()

    response = []
    for network in client.networks.list():

        custom_stuff = {
            'Stack': ''
        }

        # Figure out the stack name
        for label, v in network.attrs['Labels'].items():
            if label == LABEL_COM_DOCKER_COMPOSE_PROJECT:
                custom_stuff['Stack'] = v

        response.append({**network.attrs, **{'StackCenter': custom_stuff}})

    return jsonify(response)


# This is needed for the Vue frontend to work. Just hitting /containers would
# result in a 404 unless we throw the Vue app in front to handle the request
# with its router module
@stackcenterapp.route('/<path:path>', methods=['GET', 'OPTIONS'])
def catch_all(path):
    return root()


if __name__ == '__main__':
    stackcenterapp.run(host='0.0.0.0')
