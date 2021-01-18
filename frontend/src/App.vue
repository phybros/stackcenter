<template>
  <v-app>
    <v-navigation-drawer app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            Stack Center
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list nav dense>
        <v-list-item-group>
          <v-list-item :to="{ name: 'Stacks' }">
            <v-list-item-icon>
              <v-icon>mdi-cube-unfolded</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Stacks</v-list-item-title>
          </v-list-item>

          <v-list-item :to="{ name: 'Containers' }">
            <v-list-item-icon>
              <v-icon>mdi-cube-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Containers</v-list-item-title>
          </v-list-item>

          <v-list-item :to="{ name: 'Networks' }">
            <v-list-item-icon>
              <v-icon>mdi-lan</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Networks</v-list-item-title>
          </v-list-item>

          <v-list-item :to="{ name: 'Volumes' }">
            <v-list-item-icon>
              <v-icon>mdi-server</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Volumes</v-list-item-title>
          </v-list-item>

          <v-list-item :to="{ name: 'Images' }">
            <v-list-item-icon>
              <v-icon>mdi-image-multiple-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Images</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>{{ $route.meta.title }}</v-toolbar-title>


      <v-progress-linear
        :active="this.$store.state.appLoading"
        :indeterminate="this.$store.state.appLoading"
        :hidden="!this.$store.state.appLoading"
        absolute
        bottom
        color="blue"
      ></v-progress-linear>

      <v-spacer></v-spacer>

       <v-btn icon @click="darkMode()">
        <v-icon>mdi-moon-waxing-crescent</v-icon>
      </v-btn>

      <!-- <v-menu bottom left>
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon v-bind="attrs" v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item :to="{ name: 'Containers' }">
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>-->
    </v-app-bar> 

    <!-- Sizes your content based upon application components -->
    <v-main>
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  }),

  methods: {
    darkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    }
  }
};
</script>
