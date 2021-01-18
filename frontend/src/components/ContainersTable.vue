<template>
  <div>
    <v-card class="ma-2">
      <v-card-title>
        Containers
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        v-model="selected"
        :headers="headers"
        :search="search"
        :items="containers"
        :items-per-page="10"
        :loading="this.$store.state.appLoading"
        loading-text="Loading containers..."
        sort-by="Name"
        show-select
        item-key="Id"
      >
        <template v-slot:item.State.Status="{ item }">
          <v-chip :color="getColor(item.State.Status)" dark small>
            {{ item.State.Status }}
          </v-chip>
        </template>
        <template v-slot:item.Name="{ item }">
          <router-link
            class="text-decoration-none"
            :to="{ name: 'Container', params: { container_id: item.Id } }"
            >{{ item.Name }}</router-link
          >
        </template>
      </v-data-table>
    </v-card>

    <ul>
      <li v-for="s in selected" :key="s">{{ s.Id }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Containers",

  components: {},

  props: ["containers"],

  data: () => ({
    search: "",
    selected: [],
    headers: [
      { text: "Name", value: "Name" },
      { text: "State", value: "State.Status" },
      { text: "Stack", value: "StackCenter.Stack" },
      { text: "Image", value: "Config.Image" },
    ],
  }),

  mounted() {
    //this.containers = this.props.containers;
  },

  methods: {
    getColor(state) {
      if (state == "running") return "green";
      else if (state == "exited") return "red";
      else return "grey";
    },
  },
};
</script>
