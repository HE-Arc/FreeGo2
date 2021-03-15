<template>
  <div class="fridge">
    <Head></Head>

    <v-card>
      
      <v-card-title>
        <v-btn icon @click="isFavorite = !isFavorite">
          <v-icon color="primary" large>{{ isFavorite ? 'mdi-star' : 'mdi-star-outline' }}</v-icon>
        </v-btn>{{ APIData.name }}
      </v-card-title>
      <v-card-text>{{ APIData.my_maps_description }}</v-card-text>
      <v-card-text>{{ APIData.manager_description }}</v-card-text>

      <v-container>
        <v-row align="center" no-gutters>
          <v-col>
            <v-carousel v-model="model">
              <v-carousel-item v-for="picture in APIData.pictures" :key=picture.image>
                <v-img v-bind:src="picture.image" :aspect-ration="3/4" max-width="180"></v-img>>
              </v-carousel-item>
            </v-carousel>
          </v-col>

          <v-col>
            <v-card>
              <v-card-title>Menus</v-card-title>
              <v-card-text>{{ APIData.menu_list }}</v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
      
    </v-card>

    <Navbar></Navbar>
  </div>
</template>

<script>
  import Navbar from '../components/Navbar'
  import Head from '../components/Head'
  import { getAPI } from '../axios-api'
  import { mapState } from 'vuex'

  export default {
    name: 'Fridge',

    components: {
      Navbar,
      Head,
    },
    
    data: () => ({
      isFavorite: false,
      model: 0
    }),

    computed: mapState(['APIData']),
    created () {
      getAPI.get(((this.$route.params.fridgeId) ? '/fridge/'.concat(this.$route.params.fridgeId) : '/fridge/'), )
      .then(response => {
        this.$store.state.APIData = response.data
      })
      .catch(err => {
        console.log(err)
      })
    },
  }
</script>

<style scoped>

</style>