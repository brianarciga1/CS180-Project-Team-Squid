import { createRouter, createWebHistory } from 'vue-router'
import SpotifyAuth from '../components/SpotifyAuth.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/auth',
      name: 'SpotifyAuth',
      component: SpotifyAuth,
    },
  ],
})

export default router
