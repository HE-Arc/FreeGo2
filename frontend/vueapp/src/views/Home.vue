<template>
  <div class="home">
    <Head/>
    <Map/>
      <v-btn icon @click="overlay = !overlay">
        <v-icon color="primary" large>mdi-information</v-icon>
      </v-btn>

    <v-overlay :absolute="true" :value="overlay" :opacity="0.8">
      <v-card max-width="300">
        <v-img
          height="250"
          src="../../public/img/logo-free-go.jpg"
        ></v-img>
        <v-card-title>Association Free Go</v-card-title>
        <v-card-text>
          Notre association a pour but de mettre en place des réfrigérateurs libre-service afin de diminuer le gaspillage alimentaire tout en permettant d'aider les personnes dans le besoin. Elle a été créée en 2019.
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="overlay = !overlay">
            Voir les Free Go
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-overlay>

    <Navbar/>
  </div>
</template>

<script>
  import Navbar from '../components/Navbar'
  import Map from '../components/Map'
  import Head from '../components/Head'
  import { mapState } from 'vuex'

  export default {
    name: 'Home',

    components: {
      Navbar,
      Map,
      Head,
    },
    
    data() {
      return {
        overlay: mapState(['accessToken']),
      }
    },

    computed: mapState(['accessToken']),
  }
</script>

<style scoped>

</style>