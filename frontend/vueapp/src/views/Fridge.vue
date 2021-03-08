<template>
  <div class="fridge">
    <Head></Head>
    <div class="album py-5 bg-light">
      <div class="container">
        <div class="row">
          <div v-for="fridge in APIData" :key="fridge.id" class="col-md-4">
            <div class="card mb-4 box-shadow">
              <img class="card-img-top" src="https://via.placeholder.com/150x100" alt="Card image cap">
              <div class="card-body">
                <h4><a class="text-secondary">{{ fridge.name }}</a></h4>
                <div class="d-flex justify-content-between align-items-center"></div>
                <div class="btn-group">
                  <router-link :to = "{ name:'donations' }" class="btn btn-sm btn-outline-primary" role="button" aria-pressed="true" exact>Voir</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
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