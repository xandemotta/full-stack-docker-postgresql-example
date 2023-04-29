import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'

import '@/assets/base.css'

const app = createApp(App)

const vuetify = createVuetify({ components })

app.use(vuetify)
app.use(router)

app.mount('#app')
