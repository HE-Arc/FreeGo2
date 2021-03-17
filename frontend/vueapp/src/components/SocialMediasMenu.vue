<template>

  <v-col>
      <v-btn icon link :to="{}" exact>
        <v-icon>mdi-facebook</v-icon>
      </v-btn>

      <v-btn icon link :to="{}" exact>
        <v-icon>mdi-instagram</v-icon>
      </v-btn>

      <v-btn icon link :to="{}" exact>
        <v-icon>mdi-twitter</v-icon>
      </v-btn>

      <v-btn icon link :to="{}" exact>
        <v-icon>mdi-linkedin</v-icon>
      </v-btn>
      
      <v-btn icon link :to="{}" exact>
        <v-icon>mdi-web</v-icon>
      </v-btn>
  </v-col>

</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'SocialMediasMenu',

    computed: mapState(['accessToken']),
  }
</script>

<style scoped>
</style>
