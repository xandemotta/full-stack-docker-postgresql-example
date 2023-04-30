<script>
import ListTasks from '@/components/ListTasks.vue'
import api from '@/stores/api'

export default {
  components: { ListTasks },
  methods: {
    async fetchTasks() {
      this.tasks = await api.todo.fetchTasks()
    },
    deleteTask() {
      this.fetchTasks()
    }
  },
  created() {
    this.fetchTasks()
  },
  data() {
    return {
      tasks: []
    }
  }
}
</script>

<template>
  <list-tasks :tasks="tasks" @delete="deleteTask" />
</template>
