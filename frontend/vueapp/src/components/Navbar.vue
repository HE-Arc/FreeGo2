<template>
  <v-bottom-navigation app grow horizontal fixed>
    <v-btn value="home" :to = "{ name:'home' }" exact>
      <span>Accueil</span>
    </v-btn>
    <v-btn value="favorites" v-if="accessToken!=null" :to = "{ name:'favorites' }" exact>
      <span>Favoris</span>
    </v-btn>
    <v-btn value="options" :to = "{ name:'options' }" exact>
      <span>Options</span>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'Navbar',
    computed: mapState(['accessToken']),
  }
</script>

<style scoped>
</style>
