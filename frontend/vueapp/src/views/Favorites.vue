<template>
  <div v-if="APIData">
    <FridgeCard v-for="fridge in APIData" v-bind:key="fridge.id" v-bind:fridge="fridge"></FridgeCard>
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
      getAPI.get('/fridge/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
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