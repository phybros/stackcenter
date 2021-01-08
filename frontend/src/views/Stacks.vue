<template>
  <div>
    <v-container>
      <v-row class="mb-6" no-gutters>
        <v-dialog scrollable v-model="newDialog" persistent max-width="1000px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark v-bind="attrs" v-on="on">
              <v-icon>mdi-plus</v-icon>
              New Stack
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">New Stack</span>
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      label="Stack Name *"
                      required
                      v-model="newStack.name"
                    ></v-text-field>
                  </v-col>
                  <v-subheader>Compose YML *</v-subheader>
                  <v-col cols="12">
                    <prism-editor
                      class="my-editor"
                      v-model="newStack.composeYml"
                      :highlight="highlighter"
                      line-numbers
                    ></prism-editor>
                  </v-col>
                </v-row>
              </v-container>
              <small>*indicates required field</small>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-btn color="red darken-1" text @click="newDialog = false">
                Cancel
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="createStack()">
                Create
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
      <v-row no-gutters>
        <v-card
          :to="{ name: 'Stack', params: { stack_id: stack.Id } }"
          class="mr-4 mb-4"
          v-for="stack in stacks"
          :key="stack.Id"
          elevation="2"
          tile
          min-width="300"
        >
          <v-card-title>
            <v-icon class="mr-1" v-if="isExternal(stack.Id)">mdi-docker</v-icon>
            <v-icon class="mr-1" v-if="!isExternal(stack.Id)">mdi-cube-unfolded</v-icon>
            {{ stack.Name }}
            <v-spacer></v-spacer>
            <v-chip x-small dark :color="stackColor(stack.Id)">{{ stackStatus(stack) }}</v-chip>
          </v-card-title>
          <v-card-text>This is where the text goes</v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-btn text>
              Full Report
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-row>

      <v-btn color="primary" elevation="2" fab large absolute bottom right>
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </v-container>

    <p>{{ createResult }}</p>
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
  name: "Stacks",

  components: {
    PrismEditor,
  },

  data: function() {
    return {
      stacks: [],
      newDialog: false,
      defaultNewStack: {
        name: "",
        composeYml:
          "version: '3'\n\nservices:\n\n  myservice:\n    image: nginx\n    container_name: webserver\n    ports:\n      - \"8080:80\"\n",
      },
      newStack: {},
      createResult: '',
    };
  },

  mounted() {
    this.newStack = this.defaultNewStack;

    axios
      .get(`${process.env.VUE_APP_API_URL}/api/stacks`)
      .then((response) => (this.stacks = response.data))
      .catch((error) => console.log(error));
  },

  methods: {
    highlighter(code) {
      return highlight(code, languages.yaml); // languages.<insert language> to return html with markup
    },

    createStack() {
      this.newDialog = false;
      axios
        .post(`${process.env.VUE_APP_API_URL}/api/stacks`, this.prepareForPost(this.newStack))
        .then((response) => {this.createResult = response.data.result})
        .catch((error) => console.log(error));
    },

    prepareForPost(stack) {
      const encodedYml = {composeYml: btoa(stack.composeYml)};
      const processedStack = {...this.newStack, ...encodedYml};
      return processedStack;
    },

    isExternal(id) {
      return id.startsWith('external:');
    },

    stackColor(id) {
      return this.isExternal(id) ? "grey" : "green";
    },

    stackStatus(stack) {
      if (this.isExternal(stack.Id)) {
        return 'external';
      } else {
        // TODO: This is fake
        return 'running';
      }
    }
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
</style>
