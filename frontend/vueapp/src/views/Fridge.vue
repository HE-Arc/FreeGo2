<template>
  <v-card v-if="fridgeData">
    
    <v-card-title>
      <v-btn icon @click="favoriteClick">
        <v-icon color="info" large>{{ isFavorite ? 'mdi-star' : 'mdi-star-outline' }}</v-icon>
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

  export default {
    name: 'Fridge',

    components: {

    },
    
    data: () => ({
      favoriteId: null,
      isFavorite: null,
      fridgeData: false,
    }),

    created () {
      // TODO: Perform concurrent requests instead ?
      getAPI.get('/fridge/'.concat(this.$route.params.fridgeId).concat('/'))
      .then(response => {
        this.fridgeData = response.data

        getAPI.get('/favorite/', {
          params: {
            user: this.$store.state.userId,
            fridge: this.fridgeData.id
          }
        })
        .then(response => {
          if (response.data[0]){
            this.isFavorite = true
            this.favoriteId = response.data[0].id
          }
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
        if (this.favoriteId) {
          getAPI.delete('/favorite/'.concat(this.favoriteId).concat('/'))
          .then(response => {
            console.log(response)
            this.isFavorite = false
            this.favoriteId = null
          })
          .catch(err => {
            console.log(err)
          })
        }
        else {
          getAPI.post('/favorite/', {
            user: this.$store.state.userId,
            fridge: this.fridgeData.id
          })
          .then(response => {
            this.isFavorite = true
            this.favoriteId = response.data
          })
          .catch(err => {
            console.log(err)
          })
        }
      }
    },
  }
</script>

<style scoped>
</style>