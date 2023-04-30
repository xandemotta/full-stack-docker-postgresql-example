<script>
import TaskItem from './TaskItem.vue'

export default {
  components: { TaskItem },
  props: {
    tasks: {
      type: Array,
      required: true
    }
  },
  methods: {
    deleteTask() {
      this.$emit('delete')
    }
  }
}
</script>

<template>
  <v-sheet width="300" class="mx-auto">
    <task-item v-for="task in tasks" :task="task" :key="task.id" @delete="deleteTask" />
  </v-sheet>
</template>
