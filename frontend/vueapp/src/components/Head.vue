<template>
  <v-app-bar app color="primary" dark>
    <v-toolbar-title>Free Go</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn value="notifications" icon :to = "{ name:'notifications' }" v-if="accessToken!=null" exact>
      <v-icon>mdi-bell</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'Head',
    computed: mapState(['accessToken']),
  }
</script>

<style scoped>
</style>
