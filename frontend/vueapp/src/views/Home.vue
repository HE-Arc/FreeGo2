<template>

  <v-row style='height: 2000px; max-height: calc(100vh - 118px);'>
    <Map style='z-index:1; max-height: calc(100% - 24px); width: 100%'/>
    <v-btn icon @click="overlay = !overlay" absolute right bottom style="z-index:2; bottom:20%;">
      <v-icon color="info" large>mdi-information</v-icon>
    </v-btn>
    <v-slider
      v-model="distance"
      hint="Afficher les Free Go à proximité"
      max="50"
      min="1"
      value="10"
      thumb-label
      inverse-label
      style='height: 24px; z-index:2;'
    >
      <template v-slot:label="">{{ distance }} km</template>
    </v-slider>

    <v-overlay :absolute="false" :value="overlay" :opacity="0.8">
      <v-card max-width="300">
        <v-img
          height="250"
          src="../../public/img/logo-free-go.jpg"
        ></v-img>
        <v-card-title>Association Free Go</v-card-title>
        <v-card-text>
          L’Association Free Go, créée dans le canton de Neuchâtel, a comme objectif de se positionner dans l’action sociale de la Suisse romande en mettant en place des réfrigérateurs libre-service. Notre mission est d’aider les personnes dans le besoin tout en contribuant à diminuer le gaspillage alimentaire.
          <br/>
          Notre action est possible grâce à l’aide d’une soixantaine de bénévoles, nos sponsors et nos partenaires locaux.
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="overlay = !overlay">
            Voir les Free Go
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-overlay>
  </v-row>

</template>

<script>
  import Map from '../components/Map'
  import { mapState } from 'vuex'

  export default {
    name: 'Home',

    components: {
      Map,
    },
    
    data() {
      return {
        overlay: null,
        distance: 10,
      }
    },

    computed: mapState(['accessToken']),

    created() {
      this.overlay = this.accessToken === null ? true : false
    },
  }
</script>

<style scoped>
</style>