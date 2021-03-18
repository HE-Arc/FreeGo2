<template>
    <v-card>
      
      <v-card-title>
        <v-btn icon @click="isFavorite = !isFavorite">
          <v-icon color="primary" large>{{ isFavorite ? 'mdi-star' : 'mdi-star-outline' }}</v-icon>
        </v-btn>
        {{ APIData.name }}
      </v-card-title>
      <v-card-text>{{ APIData.my_maps_description }}</v-card-text>
      <v-card-text>{{ APIData.manager_description }}</v-card-text>

      <v-carousel>
        <v-carousel-item v-for="picture in APIData.pictures" :key=picture.image>
          <v-img v-bind:src="picture.image" :aspect-ration="3/4"></v-img>
        </v-carousel-item>
      </v-carousel>
      <v-treeview :items="APIData.menu_list.items"></v-treeview>
      
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