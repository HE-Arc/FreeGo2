<template>

  <v-col>
    <v-list>
      <v-list-item link :to="{ name:'donations' }" exact>
        <v-list-item-content>
          <v-list-item-title>Donations</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item link :to="{ name:'contactUs' }" exact>
        <v-list-item-content>
          <v-list-item-title>Nous contacter</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item link :to="{ name:'manageFridge' }" exact>
        <!-- TODO: ManageFridge should only be available to Manager role -->
        <v-list-item-content>
          <v-list-item-title>Gérer mon Free Go</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-if="accessToken==null" link :to="{ name:'login' }" exact>
        <v-list-item-content>
          <v-list-item-title>Se connecter</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-else link :to="{ name:'logout' }" exact>
        <v-list-item-content>
          <v-list-item-title>Se déconnecter</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-col>

</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'OptionsMenu',
    computed: mapState(['accessToken']),
  }
</script>

<style scoped>

</style>
