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
      path: '/options',
      name: 'options',
      component: () => import('../views/TestPageView.vue')
    },
    {
      path: '/malauth',
      name: 'malauth',
      component: () => import('../views/MalAuthPage.vue')
    }
  ]
})

export default router
