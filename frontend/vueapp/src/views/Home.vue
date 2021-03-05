<template>
  <div class="home">
    <Head v-bind:isUserConnected=isUserConnected></Head>
    <p v-show="!isUserConnected">Notre association a pour but de mettre en place des réfrigérateurs libre-service afin de diminuer le gaspillage alimentaire tout en permettant d'aider les personnes dans le besoin. Elle a été créée en 2019.</p>
    <Map></Map>
    <Navbar></Navbar>
  </div>
</template>

<script>
  import Navbar from '../components/Navbar'
  import Map from '../components/Map'
  import Head from '../components/Head'

  export default {
    name: 'Home',
    data() {
      return {
        //TODO: Change isUserConnected by actual user state
        isUserConnected: true,
      }
    },
    components: {
      Navbar,
      Map,
      Head,
    },
  }
</script>

<style scoped>

</style>