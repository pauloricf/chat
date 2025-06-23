<template>
  <div class="fixed inset-0 bg-white bg-opacity-40 flex items-center justify-center z-50">
    <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-sm">
      <h2>Criar novo grupo</h2>
      <input
        type="text"
        placeholder="Nome do grypo"
        v-model="localGroupName"
        class="w-full px-4 py-2 rounded-2xl border border-gray-300 mb-4"
      />
      <div>
        <label>Adicionar membros</label>
        <div v-for="user in users" :key="user.id" class="flex items-center mb-2">
          <input type="checkbox" :value="user.id" v-model="localSelectedUserIds" class="mr-2" />
          <span>{{ user.username }}</span>
        </div>
      </div>
      <div class="flex justify-end gap-2 mt-4">
        <button
          @click="$emit('close')"
          class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold rounded-2xl px-4 py-2"
        >
          Cancelar
        </button>
        <button
          @click="emitCreate"
          class="bg-green-500 hover:bg-green-700 text-white font-bold rounded-2xl px-4 py-2"
        >
          Criar Grupo
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
const props = defineProps<{
  users: any[]
  groupName: string
  selectedUserIds: number[]
}>()
const emit = defineEmits(['close', 'create'])
const localGroupName = ref(props.groupName)
const localSelectedUserIds = ref([...props.selectedUserIds])

watch(
  () => props.groupName,
  (val) => (localGroupName.value = val),
)
watch(
  () => props.selectedUserIds,
  (val) => (localSelectedUserIds.value = [...val]),
)

function emitCreate() {
  emit('create', {
    groupName: localGroupName.value,
    selectedUserIds: localSelectedUserIds.value,
  })
}

const groupName = ref(props.groupName)
</script>
