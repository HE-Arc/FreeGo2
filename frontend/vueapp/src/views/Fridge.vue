<template>
  <v-card v-if="fridgeData">
    
    <v-card-title>
      <v-btn icon @click="favoriteClick">
        <v-icon color="primary" large>{{ isFavorite ? 'mdi-star' : 'mdi-star-outline' }}</v-icon>
      </v-btn>
      {{ fridgeData.name }}
    </v-card-title>
    <v-card-text>{{ fridgeData.my_maps_description }}</v-card-text>
    <v-card-text>{{ fridgeData.manager_description }}</v-card-text>

    <v-carousel>
      <v-carousel-item v-for="picture in fridgeData.pictures" :key=picture.image>
        <v-img v-bind:src="picture.image" :aspect-ration="3/4"></v-img>
      </v-carousel-item>
    </v-carousel>

    <v-treeview :items="fridgeData.menu_list.items"></v-treeview>
  </v-card>
</template>

<script>
  import { getAPI } from '../axios-api'
  import { mapState } from 'vuex'

  export default {
    name: 'Fridge',

    components: {

    },
    
    data: () => ({
      isFavorite: false,
      fridgeData: null,
    }),

    computed: mapState(['userId']),
    
    created () {
      getAPI.get('/fridge/'.concat(this.$route.params.fridgeId).concat('/'))
      .then(response => {
        this.fridgeData = response.data

        getAPI.get('/favorite/', {
          params: {
            user: this.$store.state.userId,
            fridge: this.fridgeData.id
          }
        })
        .then(response =>{
          console.log(response)
          this.isFavorite = response.data.isActive
        })
        .catch(err => {
          console.log(err)
        })

      })
      .catch(err => {
        console.log(err)
      })

      
    },

    methods: {
      favoriteClick() {
        getAPI.post('/favorite/', {
          fridge: this.fridgeData
        })
        .then(response => {
          console.log(response)
          this.isFavorite = !this.isFavorite
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
  }
</script>

<style scoped>
</style>