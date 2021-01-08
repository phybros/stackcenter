<template>
  <div>
    <v-treeview :items="this.containerTree"></v-treeview>
    <pre>{{ this.container }}</pre>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Container",

  components: {},

  data: function() {
    return {
      container: {},
      containerTree: {
        items: []
      },
      id: this.$route.params.container_id,
    };
  },

  mounted() {
    axios
      .get(`${process.env.VUE_APP_API_URL}/api/containers/${this.id}`)
      .then((response) => (this.container = response.data))
      .catch((error) => console.log(error));
  },
};
</script>
