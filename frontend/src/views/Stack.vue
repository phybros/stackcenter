<template>
  <div>
    <v-card class="ma-2">
      <v-card-title>Status</v-card-title>

      <v-simple-table>
        <template v-slot:default>
          <tbody>
            <tr>
              <td>
                <strong>Name</strong>
              </td>
              <td>
                {{ stack.Name }}
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn text>
          Stop
        </v-btn>
        <v-btn text>
          Delete
        </v-btn>
      </v-card-actions>
    </v-card>

    
    <containers-table :containers="containers"></containers-table>
  </div>
</template>

<script>
import axios from "axios";
import ContainersTable from '@/components/ContainersTable.vue';

export default {
  name: "Stack",

  components: {ContainersTable},

  data: function() {
    return {
      stack: {},
      containers: [],
      id: this.$route.params.stack_id,
    };
  },

  mounted() {
    axios
      .get(`${process.env.VUE_APP_API_URL}/api/stacks/${this.id}`)
      .then((response) => (this.stack = response.data))
      .catch((error) => console.log(error));
    axios
      .get(`${process.env.VUE_APP_API_URL}/api/stacks/${this.id}/containers`)
      .then((response) => (this.containers = response.data))
      .catch((error) => console.log(error));
  },
};
</script>
