<template>
  <div class="register-container">
    <h2>Cadastro</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Usuário" required />
      <input v-model="nome" placeholder="Nome completo" required />
      <input v-model="email" type="email" placeholder="E-mail" required />
      <input v-model="password" type="password" placeholder="Senha" required />
      <button type="submit">Cadastrar</button>
      <p class="login-link">Já tem conta? <RouterLink to="/login">Entrar</RouterLink></p>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const username = ref('');
const nome = ref('');
const email = ref('');
const password = ref('');
const error = ref('');
const router = useRouter();

const register = async () => {
  try {
    await axios.post('http://localhost:8000/register', {
      username: username.value,
      nome: nome.value,
      email: email.value,
      password: password.value
    });
    router.push('/login');
  } catch (e) {
    error.value = 'Erro ao cadastrar. Tente outro usuário ou e-mail.';
  }
};
</script>

<style scoped>
.register-container {
  max-width: 350px;
  margin: 80px auto;
  padding: 2rem;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 16px #0001;
  display: flex;
  flex-direction: column;
  align-items: center;
}
input {
  width: 100%;
  margin: 8px 0;
  padding: 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
}
button {
  width: 100%;
  padding: 10px;
  background: #25d366;
  color: #fff;
  border: none;
  border-radius: 6px;
  font-weight: bold;
  margin-top: 10px;
  cursor: pointer;
}
button:hover {
  background: #128c7e;
}
.login-link {
  margin-top: 1rem;
  font-size: 0.95em;
}
.error {
  color: #d32f2f;
  margin-top: 0.5rem;
}
</style>
