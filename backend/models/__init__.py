from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Stack(db.Model):
    """A StackCenter stack.

    A StackCenter stack attaches some other metadata such as the original YAML
    that was used to create the stack. This allows for online editing and
    recreating of the stack to happen via the API.
    """
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50))
    compose_yml = db.Column(db.Text)
