import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/auth',
      name: 'auth',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/SpotAuthPage.vue')
    },
    {
      path: '/congrats',
      name: 'congrats',
      component: () => import('../views/Congrats.vue')
    },
    {
      path: '/options',
      name: 'options',
      component: () => import('../views/Options.vue')
    },
    {
      path: '/malauth',
      name: 'malauth',
      component: () => import('../views/MalAuthPage.vue')
    },
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    }
  ]
})

export default router
