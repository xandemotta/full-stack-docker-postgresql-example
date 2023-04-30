<script>
import { RouterView } from 'vue-router'
import NavbarItem from './components/NavbarItem.vue'

export default {
  components: {
    RouterView,
    NavbarItem
  }
}
</script>

<template>
  <v-app>
    <v-container full-height>
      <NavbarItem />
    </v-container>
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>

<style scoped></style>
