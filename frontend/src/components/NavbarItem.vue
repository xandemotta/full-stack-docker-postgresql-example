<script>
export default {}
</script>

<template>
  <v-app-bar elevation="0">
    <v-app-bar-title>TODO's</v-app-bar-title>
    <v-btn variant="outlined" @click.prevent="$router.push('/')">List</v-btn>
    <v-btn variant="outlined" @click.prevent="$router.push('/create')" class="ml-3">Create</v-btn>
  </v-app-bar>
</template>
