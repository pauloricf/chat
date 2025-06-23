<template>
  <div class="flex-1 overflow-y-auto py-4 px-2 flex flex-col">
    <div
      v-for="msg in messages"
      :key="msg.id"
      :class="[
        'flex flex-col mb-2',
        msg.from_user_id === currentUser.id ? 'items-end' : 'items-start'
      ]"
    >
      <div
        :class="[
          'rounded-2xl px-4 py-2 max-w-[60%] shadow text-base',
          msg.from_user_id === currentUser.id ? 'bg-green-100' : 'bg-white'
        ]"
      >
        <span
          class="font-bold mr-1"
        >
          <template v-if="msg.from_user_id === currentUser.id">Você:</template>
          <template v-else>{{ contactUser?.nome || contactUser?.username || 'Contato' }}:</template>
        </span>
        {{ msg.content }}
      </div>
      <div class="text-xs text-gray-500 mt-1">
        {{ msg.created_at ? new Date(msg.created_at).toLocaleTimeString() : '' }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{ messages: any[], currentUser: any, contactUser: any }>();
</script>