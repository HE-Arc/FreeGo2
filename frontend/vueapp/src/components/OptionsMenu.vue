<template>
  <div class="options-menu">
    <p>
      <router-link :to = "{ name:'donations' }" tag="button" exact>Donations</router-link>
      <router-link :to = "{ name:'contactUs' }" tag="button" exact>Nous contacter</router-link>
      <router-link :to = "{ name:'manageFridge' }" tag="button" v-if="accessToken!=null" exact>Gérer mon Free Go</router-link>
      <!-- TODO: ManageFridge should only be available to Manager role -->
      <router-link :to = "{ name:'login' }" tag="button" v-if="accessToken==null" exact>Se connecter</router-link>
      <router-link :to = "{ name:'logout' }" tag="button" v-else exact>Se déconnecter</router-link>
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
