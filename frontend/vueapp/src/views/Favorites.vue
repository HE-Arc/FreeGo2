<template>
  <div v-if="APIData">
    <FridgeCard v-for="favorite in APIData" v-bind:key="favorite.fridge" v-bind:fridge="favorite.fridge"></FridgeCard>
  </div>
</template>

<script>
  import FridgeCard from '../components/FridgeCard'
  import { getAPI } from '../axios-api'

  export default {
    name: 'Favorites',

    components: {
      FridgeCard,
    },
    
    data: () => ({
      APIData: null,
    }),

    created () {
      getAPI.get('/favorite/', {
        params: {
          user: this.$store.state.userId
        }
      })
      .then(response => {
        this.APIData = response.data
      })
      .catch(err => {
        console.log(err)
      })
    },
  }
</script>

<style scoped>
</style>