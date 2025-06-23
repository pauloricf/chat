<template>
  <form class="flex gap-2 mb-1" @submit.prevent="send">
    <input
      v-model="text"
      placeholder="Digite uma mensagem..."
      required
      class="flex-1 px-4 py-2 rounded-2xl border border-gray-300 bg-white h-12"
    />
    <button
      type="submit"
      class="bg-green-500 hover:bg-green-700 text-white font-bold rounded-2xl px-4 py-2 h-12"
    >
      Enviar
    </button>
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