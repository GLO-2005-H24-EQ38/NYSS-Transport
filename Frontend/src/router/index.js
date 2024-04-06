import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView/HomeView.vue'
import LogIn from "@/views/Authentication/LogIn.vue";
import SignUp from "@/views/Authentication/SignUp.vue";
import AdminView from "@/views/HomeView/AdminView.vue";
import UserView from "@/views/userView/UserView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LogIn
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminView
    },
    {
      path: '/user',
      name: 'user',
      component: UserView
    },
  ]
})

export default router
