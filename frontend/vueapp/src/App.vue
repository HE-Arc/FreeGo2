<template>
  <v-app>
    <Head/>
    <v-main>
      <v-container fluid>
        <router-view>
          <Home/>
        </router-view>
      </v-container>
    </v-main>
      <Navbar/>
  </v-app>
</template>

<script>
  import Home from './views/Home'
  import Navbar from './components/Navbar'
  import Head from './components/Head'
  import Vue from 'vue'
  import Vuelidate from 'vuelidate'
  Vue.use(Vuelidate)
  Vue.config.devtools = true

  export default {
    name: 'App',

    components: {
      Home,
      Navbar,
      Head,
    },

    watch: {
      title: {
        immediate: true,
        handler() {
          document.title = "Free Go";
        }
      }
    },

    data: () => ({
      //
    }),
  };
</script>
