<template>
  <div class="chat-layout">
    <UserList :users="filteredUsers" :selectedUser="selectedUser" @selectUser="selectUser" />
    <div class="chat-area" v-if="selectedUser">
      <MessageList :messages="messages" :currentUser="currentUser" />
      <MessageInput @sendMessage="sendMessage" />
    </div>
    <div v-else class="chat-placeholder">Selecione um contato para começar a conversar.</div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import UserList from '../components/UserList.vue';
import MessageList from '../components/MessageList.vue';
import MessageInput from '../components/MessageInput.vue';
import { useRouter } from 'vue-router';

const users = ref<any[]>([]);
const selectedUser = ref<any>(null);
const messages = ref<any[]>([]);
const currentUser = ref<any>(null);
const router = useRouter();

const fetchUsers = async () => {
  const token = localStorage.getItem('token');
  try {
    const res = await axios.get('http://localhost:8000/users', { headers: { Authorization: `Bearer ${token}` } });
    users.value = res.data;
    // Supondo que o backend retorna o usuário logado em /me
    const me = await axios.get('http://localhost:8000/me', { headers: { Authorization: `Bearer ${token}` } });
    currentUser.value = me.data;
  } catch (e) {
    // Se der erro de autenticação, faz logout automático
    localStorage.removeItem('token');
    router.push('/login');
  }
};

const filteredUsers = computed(() => {
  if (!currentUser.value) return users.value;
  return users.value.filter((u: any) => u && currentUser.value && u.id !== currentUser.value.id);
});

const selectUser = async (user: any) => {
  selectedUser.value = user;
  await fetchMessages();
};

const fetchMessages = async () => {
  if (!selectedUser.value || !('id' in selectedUser.value)) return;
  const token = localStorage.getItem('token');
  const res = await axios.get(`http://localhost:8000/messages/${selectedUser.value.id}`, { headers: { Authorization: `Bearer ${token}` } });
  messages.value = res.data;
};

const sendMessage = async (text: string) => {
  if (!selectedUser.value || !('id' in selectedUser.value) || !currentUser.value) return;
  const token = localStorage.getItem('token');
  await axios.post('http://localhost:8000/messages', {
    from_user_id: currentUser.value.id,
    to_user_id: selectedUser.value.id,
    content: text
  }, { headers: { Authorization: `Bearer ${token}` } });
  await fetchMessages();
};

onMounted(fetchUsers);
</script>

<style scoped>
.chat-layout {
  display: flex;
  height: 90vh;
  background: #f0f2f5;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 16px #0001;
}
.chat-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: #e5ddd5;
  padding: 0 0.5rem;
}
.chat-placeholder {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #888;
  font-size: 1.2em;
}
</style>
