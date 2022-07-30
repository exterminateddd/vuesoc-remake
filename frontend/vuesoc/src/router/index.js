import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/auth',
    name: 'Authentication',
    component: () => import('../views/AuthenticationView.vue')
  },
  {
    path: '/logout',
    name: 'LogoutDummy',
    component: () => import('../views/LogoutDummy.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
