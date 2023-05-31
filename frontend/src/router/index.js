import Vue from "vue";
import VueRouter from "vue-router";
//import HomeView from "../views/HomeView.vue";
import HomeView from "../views/HomeView.vue";
import SubjectView from "../views/SubjectView.vue";
import About from "../views/AboutView.vue";
import UsersView from "../views/UsersView.vue";
import CustomersView from "../views/CustomersView.vue";
import DashboardView from "../views/DashboardView.vue";
import AccountsView from "../views/AccountsView.vue";
import LoginView from "../views/LoginView.vue";

/* eslint-disable */
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "HomeView",
    component: HomeView,
    meta: {
      requiresAuth: false, 
    },
  },
  {
    path: "/subject/:subject_name",
    name: "SubjectView",
    component: SubjectView,
    meta: {
      requiresAuth: false, 
    },
  },
  {
    path: "/dash",
    name: "DashboardView",
    component: DashboardView,
    meta: {
      requiresAuth: true, // add this meta field to routes that require authentication
    },
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/about",
    name: "about",
    component: About,
    meta: {
      requiresAuth: true, 
    },
  },
  {
    path: "/users",
    name: "UsersView",
    component: UsersView,
    meta: {
      requiresAuth: true, 
    },
  },
  {
    path: "/customers",
    name: "CustomersView",
    component: CustomersView,
    meta: {
      requiresAuth: true, 
    },
  },
  {
    path: "/accounts",
    name: "AccountsView",
    component: AccountsView,
    meta: {
      requiresAuth: true, 
    },
  },
  {
    path: "/dashboard",
    name: "DashboardView",
    component: DashboardView,
    meta: {
      requiresAuth: false,
    },
  },
  {
    path: "/test",
    name: "test",
    component: () =>
      import("../components/TestCom.vue"),
  },
];

const router = new VueRouter({
  base: process.env.BASE_URL,
  routes,
});


// to check use is logged in before each rout
router.beforeEach((to, from, next) => {
  if (to.matched.some((route) => route.meta.requiresAuth)) {
    const token = localStorage.getItem('access_token')
    if (!token) {
      // if access token is not found, redirect to login page
      next({ name: 'login' })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router;
