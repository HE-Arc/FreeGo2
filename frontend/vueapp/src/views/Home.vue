<template>
  <div class="home">
    <Head></Head>
    <p v-if="accessToken==null">Notre association a pour but de mettre en place des réfrigérateurs libre-service afin de diminuer le gaspillage alimentaire tout en permettant d'aider les personnes dans le besoin. Elle a été créée en 2019.</p>
    <Map/>
    <Navbar></Navbar>
  </div>
</template>

<script>
  import Navbar from '../components/Navbar'
  import Map from '../components/Map'
  import Head from '../components/Head'
  import { mapState } from 'vuex'

  export default {
    name: 'Home',
    computed: mapState(['accessToken']),
    components: {
      Navbar,
      Map,
      Head,
    },
  }
</script>

<style scoped>

</style>