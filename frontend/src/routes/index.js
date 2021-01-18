import Vue from "vue";
import VueRouter from "vue-router";

import Stacks from "@/views/Stacks";
import Stack from "@/views/Stack";
import Containers from "@/views/Containers";
import Container from "@/views/Container";
import Networks from "@/views/Networks";
import Volumes from "@/views/Volumes";
import Images from "@/views/Images";

Vue.use(VueRouter);

// Set up the actual router object
var router = new VueRouter({
  mode: "history",
  // Add a catchall route
  routes: [
    {
      path: "/",
      name: "Home",
      component: Stacks,
      meta: {
        title: "Home",
      },
    },
    {
      path: "/stacks",
      name: "Stacks",
      component: Stacks,
      meta: {
        title: "Stacks",
      },
    },
    {
      path: "/stacks/:stack_id",
      name: "Stack",
      component: Stack,
      meta: {
        title: "Stack Details",
      },
    },
    {
      path: "/containers",
      name: "Containers",
      component: Containers,
      meta: {
        title: "Containers",
      },
    },
    {
      path: "/containers/:container_id",
      name: "Container",
      component: Container,
      meta: {
        title: "Container Details",
      },
    },
    {
      path: "/networks",
      name: "Networks",
      component: Networks,
      meta: {
        title: "Networks",
      },
    },
    {
      path: "/volumes",
      name: "Volumes",
      component: Volumes,
      meta: {
        title: "Volumes",
      },
    },
    {
      path: "/images",
      name: "Images",
      component: Images,
      meta: {
        title: "Images",
      },
    },
  ],
});

export default router;
