<script>
import api from '@/stores/api'
import router from '@/router'

export default {
  data() {
    return {
      valid: false,
      content: '',
      contentRules: [
        (value) => {
          if (value) return true
          return "Field can't be empty"
        }
      ]
    }
  },
  methods: {
    async createTask() {
      await api.todo.createTask(this.content)
    },
    submitForm() {
      this.createTask()
      router.push('/')
    }
  }
}
</script>

<template>
  <v-sheet width="300" class="mx-auto">
    <v-form v-model="valid" @submit.prevent>
      <v-text-field
        :rules="contentRules"
        v-model="content"
        label="Task content"
        variant="outlined"
        required
      ></v-text-field>
      <v-btn variant="outlined" type="submit" block class="mt-2" @click.prevent="submitForm"
        >Submit</v-btn
      >
    </v-form>
  </v-sheet>
</template>
