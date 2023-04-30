<script>
import api from '@/stores/api'

export default {
  data() {
    return {
      color: this.task.is_done ? 'green' : 'black'
    }
  },
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  methods: {
    async toggleDone() {
      let task = await api.todo.markDone(this.task.id)
      this.color = task.is_done ? 'green' : 'black'
    },
    async deleteTask() {
      await api.todo.delete(this.task.id)
      this.$emit('delete')
    }
  }
}
</script>

<template>
  <v-card variant="outlined" class="mb-5" :color="color">
    <v-card-title>{{ task.content }}</v-card-title>
    <v-card-actions>
      <v-btn variant="outlined" @click.prevent="toggleDone">Toggle done</v-btn>
      <v-btn variant="outlined" @click.prevent="deleteTask">Delete</v-btn>
    </v-card-actions>
  </v-card>
</template>
