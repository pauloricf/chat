<template>
  <form class="message-input" @submit.prevent="send">
    <input v-model="text" placeholder="Digite uma mensagem..." required />
    <button type="submit">Enviar</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
const text = ref('');
const emit = defineEmits(['sendMessage']);

const send = () => {
  if (!text.value.trim()) return;
  emit('sendMessage', text.value);
  text.value = '';
};
</script>

<style scoped>
.message-input {
  display: flex;
  padding: 0.5rem;
  background: #f7f7f7;
  border-top: 1px solid #eee;
}
input {
  flex: 1;
  padding: 10px;
  border-radius: 18px;
  border: 1px solid #ccc;
  margin-right: 8px;
}
button {
  background: #25d366;
  color: #fff;
  border: none;
  border-radius: 18px;
  padding: 10px 18px;
  font-weight: bold;
  cursor: pointer;
}
button:hover {
  background: #128c7e;
}
</style>
