<template>
  <v-app-bar app color="primary" dark>
    <v-toolbar-title>Free Go</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn value="notifications" icon :to = "{ name:'notifications' }" v-if="accessToken!=null" exact>
      <v-icon v-if="notificationsAmount <= 0">mdi-bell</v-icon>
      <v-icon v-else>mdi-bell-ring</v-icon>

      <v-badge
        v-if="notificationsAmount > 0"
        color="secondary"
        :content=notificationsAmount
        bottom
      ></v-badge>
    </v-btn>
  </v-app-bar>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'Head',

    data() {
      return {
        icon: '',
      }
    },

    computed: {
      ...mapState(['accessToken', 'notificationsAmount']),
    },
  }
</script>

<style scoped>
</style>
