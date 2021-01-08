<template>
  <div>
    <containers-table :containers="containers"/>
  </div>
</template>

<script>
import axios from "axios";
import ContainersTable from '@/components/ContainersTable.vue';

export default {
  name: "Containers",

  components: {
    ContainersTable,
  },

  data: () => ({
    containers: [],
  }),

  mounted() {
    axios
      .get(`${process.env.VUE_APP_API_URL}/api/containers`)
      .then((response) => (this.containers = response.data))
      .catch((error) => console.log(error));
  },

  methods: {

  },
};
</script>
