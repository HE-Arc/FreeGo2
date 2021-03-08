<template>
  <div class="head">
    <p>
      <span>Free Go</span>
      <router-link :to = "{ name:'notifications' }" v-if="accessToken!=null" exact>Notifications</router-link>
    </p>
  </div>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'Head',
    computed: mapState(['accessToken']),
  }
</script>

<style scoped>
  a {
    color: #000;
  }
</style>
