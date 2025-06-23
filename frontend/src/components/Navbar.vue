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
  <nav class="flex justify-between items-center bg-green-500 text-white px-8 py-3 rounded-b-xl shadow-md mb-6
              max-[600px]:flex-col max-[600px]:px-2 max-[600px]:py-4 max-[600px]:gap-2">
    <div class="font-bold text-lg tracking-wide">
      <RouterLink to="/chat" class="text-white no-underline hover:underline">ChatApp</RouterLink>
    </div>
    <div class="flex items-center gap-3">
      <template v-if="user">
        <span class="font-medium mr-2 bg-white/20 px-3 py-1 rounded-md">
          {{ user.username || user.nome }}
        </span>
        <button
          class="bg-white text-green-500 rounded-md px-4 py-2 font-bold transition hover:bg-green-700 hover:text-white text-base outline-none"
          @click="logout"
        >
          Sair
        </button>
      </template>
      <template v-else>
        <button
          class="bg-white text-green-500 rounded-md px-4 py-2 font-bold transition hover:bg-green-700 hover:text-white text-base outline-none"
          @click="goLogin"
        >
          Entrar
        </button>
        <button
          class="bg-transparent text-white border-2 border-white rounded-md px-4 py-2 font-bold transition hover:bg-white hover:text-green-500 text-base outline-none"
          @click="goRegister"
        >
          Cadastrar
        </button>
      </template>
    </div>
  </nav>
</template>