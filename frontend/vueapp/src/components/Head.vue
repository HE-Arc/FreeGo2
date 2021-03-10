<template>
  <v-app-bar app color="primary" dark>
    <div class="head">
      <p>
        <span>Free Go</span>
        <v-btn value="notifications" icon :to = "{ name:'notifications' }" v-if="accessToken!=null" exact>
          <v-icon>mdi-bell</v-icon>
        </v-btn>
      </p>
    </div>
  </v-app-bar>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'Head',
    computed: mapState(['accessToken']),
  }
</script>

<style scoped>
</style>
