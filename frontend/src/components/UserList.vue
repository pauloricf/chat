<template>
  <div class="user-list">
    <div v-for="user in users" :key="user.id" :class="['user-item', { selected: user.id === selectedUser?.id }]" @click="$emit('selectUser', user)">
      <div class="avatar">{{ user.username.charAt(0).toUpperCase() }}</div>
      <span>{{ user.username }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{ users: any[], selectedUser: any }>();
</script>

<style scoped>
.user-list {
  width: 260px;
  background: #fff;
  border-right: 1px solid #eee;
  padding: 1rem 0.5rem;
  overflow-y: auto;
}
.user-item {
  display: flex;
  align-items: center;
  padding: 10px;
  border-radius: 8px;
  cursor: pointer;
  margin-bottom: 6px;
  transition: background 0.2s;
}
.user-item.selected, .user-item:hover {
  background: #e5ddd5;
}
.avatar {
  width: 36px;
  height: 36px;
  background: #25d366;
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  margin-right: 12px;
  font-size: 1.2em;
}
</style>
