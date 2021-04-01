<template>
  <v-app-bar app color="primary" dark>
    <v-toolbar-title>Free Go</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn value="notifications" icon :to = "{ name:'notifications' }" v-if="accessToken!=null" exact>
      {{ notificationsAmount.notificationsAmount }}<v-icon>{{ `${icon}` }}</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'Head',

    data() {
      return {
        icon: 'mdi-bell',
      }
    },

    computed: {
      ...mapState(['accessToken', 'notificationsAmount']),
    },
  }
</script>

<style scoped>
</style>
