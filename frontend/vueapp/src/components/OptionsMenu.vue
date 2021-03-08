<template>
  <div class="options-menu">
    <p>
      <router-link :to = "{ name:'donations' }" exact>Donations</router-link>
      <router-link :to = "{ name:'contactUs' }" exact>Nous contacter</router-link>
      <router-link :to = "{ name:'manageFridge' }" v-if="accessToken!=null" exact>Gérer mon Free Go</router-link>
      <!-- TODO: ManageFridge should only be available to Manager role -->
      <router-link :to = "{ name:'login' }" v-if="accessToken==null" exact>Se connecter</router-link>
      <router-link :to = "{ name:'logout' }" v-else exact>Se déconnecter</router-link>
    </p>
  </div>
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
