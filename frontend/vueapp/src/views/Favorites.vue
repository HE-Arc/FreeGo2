<template>
  <div>
    <FridgeCard v-for="fridge in APIData" v-bind:key="fridge.id" v-bind:fridge="fridge"></FridgeCard>
  </div>
</template>

<script>
  import FridgeCard from '../components/FridgeCard'
  import { getAPI } from '../axios-api'
  import { mapState } from 'vuex'

  export default {
    name: 'Favorites',

    components: {
      FridgeCard,
    },

    computed: mapState(['APIData']),

    created () {
      getAPI.get('/fridge/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
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