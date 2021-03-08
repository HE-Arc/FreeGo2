<template>
  <div class="head">
    <p>
      <span>Free Go</span>
      <button v-if="accessToken!=null">Notifications</button>
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
