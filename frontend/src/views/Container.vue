<template>
  <div>
    <v-row justify="start" no-gutters class="mb-3">
      <v-btn class="mr-2" color="success" :disabled="!allowStart">
        <v-icon>mdi-play</v-icon>
        Start
      </v-btn>
      <v-btn class="mr-2" color="error" :disabled="!allowStop">
        <v-icon>mdi-stop</v-icon>
        Stop
      </v-btn>
      <v-btn class="mr-2" color="primary" :disabled="!allowRestart">
        <v-icon>mdi-restart</v-icon>
        Restart
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        class="mr-2"
        color="error"
        :disabled="this.$store.state.appLoading"
      >
        <v-icon>mdi-delete</v-icon>
        Remove
      </v-btn>
    </v-row>

    <v-card class="mb-3">
      <v-card-title>
        <v-icon class="mr-1">mdi-list-status</v-icon>
        Status
      </v-card-title>
      <v-card-text>
        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>ID</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>
              {{ container.Id }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Name</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>
              {{ container.Name }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Status</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>
              {{ container.State.Status }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Image</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>
              {{ container.Config.Image }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Created</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>
              {{ container.Created }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Started</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>
              {{ container.State.StartedAt }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Exited</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>
              {{ container.State.FinishedAt }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-card-text>
    </v-card>

    <v-card class="mb-3">
      <v-card-title>
        <v-icon class="mr-1">mdi-view-list</v-icon>
        Details
      </v-card-title>
      <v-card-text>
        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Cmd</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>

              <code>
                <span v-for="c in container.Config.Cmd" :key="c">
                  {{ c }}
                </span>
              </code>
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Entrypoint</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>

              <code>
                <span v-for="c in container.Config.Entrypoint" :key="c">
                  {{ c }}
                </span>
              </code>
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Labels</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>
              <v-simple-table dense>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th class="text-left">
                        Label
                      </th>
                      <th class="text-left">
                        Value
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="(value, name) in container.Config.Labels"
                      :key="name"
                    >
                      <td>{{ name }}</td>
                      <td>{{ value }}</td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Environment</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>
              <v-simple-table dense>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th class="text-left">
                        Variable
                      </th>
                      <th class="text-left">
                        Value
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="variable in container.Config.Env"
                      :key="variable"
                    >
                      <td>{{ variable.split(/=(.+)/)[0] }}</td>
                      <td>{{ variable.split(/=(.+)/)[1] }}</td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>User</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>
              {{ container.Config.User }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-card-text>
    </v-card>

    <v-card class="mb-3">
      <v-card-title>
        <v-icon class="mr-1">mdi-lan</v-icon>
        Networking
      </v-card-title>
      <v-card-text>
        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Networks</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>

              <span
                v-for="(details, network) in container.NetworkSettings.Networks"
                :key="network"
              >
              {{ network }}<br>
              </span>
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Ports</v-list-item-title>
            <v-list-item-subtitle>
              <v-skeleton-loader
                v-if="this.$store.state.appLoading"
                type="text"
                width="200"
              ></v-skeleton-loader>

              <span
                v-for="(details, containerport) in container.NetworkSettings.Ports"
                :key="containerport"
              >
              {{ containerport }}
              <v-icon>mdi-arrow-right-bold</v-icon>
              <span v-for="p in details" :key="p">
                {{ p.HostIp }}:{{ p.HostPort }}
              </span>
              <br>
              </span>
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-card-text>
    </v-card>

    <v-expansion-panels multiple v-model="panels">
      <v-expansion-panel>
        <v-expansion-panel-header>Full JSON</v-expansion-panel-header>
        <v-expansion-panel-content>
          <prism-editor
            class="my-editor"
            v-model="this.containerJson"
            :highlight="highlighter"
            readonly
            line-numbers
          ></prism-editor>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
import axios from "axios";

// import Prism Editor
import { PrismEditor } from "vue-prism-editor";
import "vue-prism-editor/dist/prismeditor.min.css"; // import the styles somewhere

// import highlighting library (you can use any library you want just return html string)
import { highlight, languages } from "prismjs/components/prism-core";
import "prismjs/components/prism-clike";
import "prismjs/components/prism-yaml";
import "prismjs/themes/prism-tomorrow.css"; // import syntax highlighting styles

export default {
  name: "Container",

  components: {
    PrismEditor,
  },

  data: function() {
    return {
      container: {},
      containerRunning: "loading",
      containerJson: "",
      panels: [],
      allowStart: false,
      allowStop: false,
      allowRestart: false,
      containerTree: {
        items: [],
      },
      id: this.$route.params.container_id,
    };
  },

  mounted() {
    this.containerRunning = "loading";
    this.$store.commit("appLoading", true);

    axios
      .get(`${process.env.VUE_APP_API_URL}/api/containers/${this.id}`)
      .then((response) => {
        this.container = response.data;
        this.containerJson = JSON.stringify(this.container, null, 2);
        this.$store.commit("appLoading", false);

        if (this.container.State.Running) {
          this.allowStart = false;
          this.allowStop = true;
          this.allowRestart = true;
        } else {
          this.allowStart = true;
          this.allowStop = false;
          this.allowRestart = false;
        }
      })
      .catch((error) => console.log(error));
  },

  methods: {
    highlighter(code) {
      return highlight(code, languages.yaml); // languages.<insert language> to return html with markup
    },
  },
};
</script>

<style>
/* required class */
.my-editor {
  /* we dont use `language-` classes anymore so thats why we need to add background and text color manually */
  background: #2d2d2d;
  color: #ccc;

  /* you must provide font-family font-size line-height. Example: */
  font-family: Fira code, Fira Mono, Consolas, Menlo, Courier, monospace;
  font-size: 14px;
  line-height: 1.5;
  padding: 5px;
}

/* optional class for removing the outline */
.prism-editor__textarea:focus,
.prism-editor__textarea:focus-visible {
  outline: none;
}

.prism-editor__editor {
  white-space: pre !important;
}
.prism-editor__container {
  overflow-x: scroll !important;
}
</style>
