<template>
  <div>
    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">
              Name
            </th>
            <th class="text-left">
              Stack
            </th>
            <th class="text-left">
              Driver
            </th>
            
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in networks" :key="item.Id">
            <td>
              <router-link :to="{ name: 'Networks' }">
                {{ item.Name }}
              </router-link>
            </td>
            <td>
              {{ item.StackCenter.Stack }}
            </td>
            <td>
              {{ item.Driver }}
            </td>
           
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Networks",

  components: {},

  data: () => ({
    networks: [],
  }),

  mounted() {
    axios
      .get(`${process.env.VUE_APP_API_URL}/api/networks`)
      .then((response) => (this.networks = response.data))
      .catch((error) => console.log(error));
  },
};
</script>
