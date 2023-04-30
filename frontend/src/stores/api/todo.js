import axios from 'axios'
import { apiUrl } from '@/consts'

const todoAPI = {
  headers: {
    'Access-Control-Allow-Origin': '*'
  },
  async fetchTasks() {
    let data = await axios
      .get(`${apiUrl}/todo/all/`, { headers: this.headers })
      .then((res) => res.data)
    return data
  },
  async createTask(content) {
    let data = await axios
      .post(`${apiUrl}/todo/create`, { content: content }, { headers: this.headers })
      .then((res) => res.data)
    return data
  },
  async delete(taskId) {
    let data = await axios
      .delete(`${apiUrl}/todo/delete`, { params: { pk: taskId }, headers: this.headers })
      .then((res) => res.data)
    return data
  },
  async markDone(taskId) {
    let data = await axios
      .put(`${apiUrl}/todo/toggle_is_done`, { pk: taskId }, { headers: this.headers })
      .then((res) => res.data)
    return data
  }
}

export default todoAPI
