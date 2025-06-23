<template>
  <div class="user-list">
    <div>
      <button
        class="bg-green-500 hover:bg-green-700 text-white font-bold rounded-2xl px-4 py-2 mb-4 w-full cursor-pointer"
        @click="showModal = true"
      >
        Criar Grupo
      </button>
    </div>
    <div
      v-for="user in users"
      :key="user.id"
      :class="['user-item', { selected: user.id === selectedUser?.id }]"
      @click="$emit('selectUser', user)"
    >
      <div class="avatar">{{ user.username.charAt(0).toUpperCase() }}</div>
      <span>{{ user.username }}</span>
    </div>

    <GroupModal
      v-if="showModal"
      :users="users"
      :selectedUserIds="selectedUserIds"
      :groupName="groupName"
      @close="closeModal"
      @createGroup="$emit('createGroup', groupName, selectedUserIds)"
    />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import GroupModal from './GroupModal.vue'
defineProps<{ users: any[]; selectedUser: any }>()

const showModal = ref(false)
const groupName = ref('')
const selectedUserIds = ref<number[]>([])

function closeModal() {
  showModal.value = false
  groupName.value = ''
  selectedUserIds.value = []
}
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
.user-item.selected,
.user-item:hover {
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
