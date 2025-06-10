<template>
  <div class="message-list">
    <div v-for="msg in messages" :key="msg.id" :class="['message', { 'me': msg.from_user_id === currentUser.id }]">
      <div class="bubble">
        <span v-if="msg.from_user_id === currentUser.id" class="sender-label">Você:</span>
        <span v-else class="sender-label">{{ contactUser?.nome || contactUser?.username || 'Contato' }}:</span>
        {{ msg.content }}
      </div>
      <div class="meta">{{ msg.created_at ? new Date(msg.created_at).toLocaleTimeString() : '' }}</div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{ messages: any[], currentUser: any, contactUser: any }>();
</script>

<style scoped>
.message-list {
  flex: 1;
  overflow-y: auto;
  padding: 1rem 0.5rem;
  display: flex;
  flex-direction: column;
}
.message {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 10px;
}
.message.me {
  align-items: flex-end;
}
.bubble {
  background: #fff;
  padding: 10px 16px;
  border-radius: 18px;
  max-width: 60%;
  box-shadow: 0 1px 4px #0001;
  font-size: 1.05em;
}
.message.me .bubble {
  background: #dcf8c6;
}
.meta {
  font-size: 0.8em;
  color: #888;
  margin-top: 2px;
}
.sender-label {
  font-weight: bold;
  margin-right: 5px;
}
</style>
