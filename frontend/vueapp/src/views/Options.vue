<template>
  <div class="options">
    <Head v-bind:isUserConnected=isUserConnected></Head>
    <Navbar v-bind:isUserConnected=isUserConnected></Navbar>
  </div>
</template>

<script>
  import Navbar from '../components/Navbar'
  import Head from '../components/Head'

  export default {
    name: 'Options',
    data() {
      return {
        //TODO: Change isUserConnected by actual user state
        isUserConnected: false,
      }
    },
    components: {
      Navbar,
      Head,
    },
  }
</script>

<style scoped>

</style>