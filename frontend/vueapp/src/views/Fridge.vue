<template>
  <div class="fridge">
    <Head></Head>
    <p>TODO: Détails du frigo</p>
    <p>{{ APIData }}</p>
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