<template>
  <v-app>
    <v-main>
      <router-view>
        <Home/>
      </router-view>
    </v-main>
  </v-app>
</template>

<script>
  import Home from './views/Home'
  import Vue from 'vue'
  import Vuelidate from 'vuelidate'
  Vue.use(Vuelidate)

  export default {
    name: 'App',

    components: {
      Home,
    },

    data: () => ({
      //
    }),
  };
</script>
