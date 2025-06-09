<script setup lang="ts">
import { RouterLink, useRouter, useRoute } from 'vue-router';
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';

const router = useRouter();
const route = useRoute();
const user = ref<any>(null);

const fetchUser = async () => {
  const token = localStorage.getItem('token');
  if (!token) {
    user.value = null;
    return;
  }
  try {
    const res = await axios.get('http://localhost:8000/me', { headers: { Authorization: `Bearer ${token}` } });
    user.value = res.data;
  } catch (err: any) {
    // Se o token expirou ou for inválido, faz logout automático
    user.value = null;
    localStorage.removeItem('token');
    if (route.path !== '/login' && route.path !== '/register') {
      router.push('/login');
    }
  }
};

const logout = () => {
  localStorage.removeItem('token');
  user.value = null;
  router.push('/login');
};

function goLogin() {
  user.value = null;
  router.push({ path: '/login', query: { t: Date.now() } });
}
function goRegister() {
  user.value = null;
  router.push({ path: '/register', query: { t: Date.now() } });
}

onMounted(fetchUser);
watch(() => route.fullPath, fetchUser);
</script>

<template>
  <nav class="navbar">
    <div class="nav-left">
      <RouterLink to="/chat" class="logo">ChatApp</RouterLink>
    </div>
    <div class="nav-right">
      <template v-if="user">
        <span class="username">{{ user.username || user.nome }}</span>
        <button class="btn" @click="logout">Sair</button>
      </template>
      <template v-else>
        <button class="btn" @click="goLogin">Entrar</button>
        <button class="btn btn-outline" @click="goRegister">Cadastrar</button>
      </template>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #25d366;
  color: #fff;
  padding: 0.7rem 2rem;
  border-radius: 0 0 12px 12px;
  box-shadow: 0 2px 8px #0002;
  margin-bottom: 1.5rem;
}
.logo {
  font-weight: bold;
  font-size: 1.3em;
  color: #fff;
  text-decoration: none;
  letter-spacing: 1px;
}
.nav-right {
  display: flex;
  align-items: center;
  gap: 0.7rem;
}
.username {
  font-weight: 500;
  margin-right: 0.5rem;
  background: #fff3;
  padding: 4px 12px;
  border-radius: 8px;
}
.btn {
  background: #fff;
  color: #25d366;
  border: none;
  border-radius: 6px;
  padding: 7px 18px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
  font-size: 1em;
  outline: none;
}
.btn:hover {
  background: #128c7e;
  color: #fff;
}
.btn-outline {
  background: transparent;
  color: #fff;
  border: 2px solid #fff;
}
.btn-outline:hover {
  background: #fff;
  color: #25d366;
}
@media (max-width: 600px) {
  .navbar {
    flex-direction: column;
    padding: 1rem 0.5rem;
    gap: 0.5rem;
  }
  .logo {
    font-size: 1.1em;
  }
  .btn {
    padding: 6px 10px;
    font-size: 0.95em;
  }
}
</style>

