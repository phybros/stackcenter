import Vue from "vue";
import Vuex from "vuex";
import App from "./App.vue";

Vue.config.productionTip = false;

Vue.use(Vuex);

import router from "./routes";
import vuetify from "./plugins/vuetify";

const store = new Vuex.Store({
  state: {
    appLoading: false,
    pageTitle: "",
  },
  mutations: {
    appLoading(state, loading) {
      state.appLoading = loading;
    },
    pageTitle(state, title) {
      state.pageTitle = title;
    },
  },
});

const app = new Vue({
  render: (h) => h(App),
  vuetify,
  router: router,
  store: store,
});

app.$mount("#app");
