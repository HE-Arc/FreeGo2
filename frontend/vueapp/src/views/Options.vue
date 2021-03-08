<template>
  <div class="options">
    <Head></Head>
    <OptionsMenu></OptionsMenu>
    <Navbar></Navbar>
  </div>
</template>

<script>
  import Navbar from '../components/Navbar'
  import Head from '../components/Head'
  import OptionsMenu from '../components/OptionsMenu'

  export default {
    name: 'Options',
    components: {
      Navbar,
      OptionsMenu,
      Head,
    },
  }
</script>

<style scoped>

</style>