import { createRouter, createWebHistory } from 'vue-router'
import ListTasksView from '@/views/ListTasksView.vue'
import CreateTaskView from '@/views/CreateTaskView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'listTasks',
      component: ListTasksView
    },
    {
      path: '/create',
      name: 'createTask',
      component: CreateTaskView
    }
  ]
})

export default router
