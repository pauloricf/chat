import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ChatView from '../views/ChatView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
    },
    {
      path: '/chat',
      name: 'chat',
      component: ChatView,
      meta: { requiresAuth: true },
    },
  ],
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  // Permitir acesso livre a login e register se não houver token
  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else if (to.path === '/login' || to.path === '/register') {
    // Só redireciona para /chat se o token existir E for válido
    if (token) {
      // Testar se o token é válido (opcional: pode fazer uma chamada ao backend aqui)
      next()
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
