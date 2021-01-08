import Vue from "vue";
import App from "./App.vue";

Vue.config.productionTip = false;

// import VueMaterial from "vue-material";
// import "vue-material/dist/vue-material.min.css";
// import "vue-material/dist/theme/default.css";
// Vue.use(VueMaterial);

import router from "./routes";
import vuetify from "./plugins/vuetify";

const app = new Vue({
  render: (h) => h(App),
  vuetify,
  router: router,
});

app.$mount("#app");
