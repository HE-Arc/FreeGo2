<template>
  <div class="nav-bar">
    <nav class="navbar navbar-expand-lg navbar-light bg-white nav-1">
      <div class="container mw-0 px-3">
        <a href="#" class="navbar-brand"></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link :to = "{ name:'home' }" exact>Accueil</router-link>
            </li>
            <li class="nav-item" v-if="accessToken!=null">
              <router-link :to = "{ name:'favorites' }" exact>Favoris</router-link>
            </li>
            <li class="nav-item">
              <router-link :to = "{ name:'options' }" exact>Options</router-link>
            </li>
          </ul>
        </div>

      </div>
    </nav>
  </div>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'Navbar',
    computed: mapState(['accessToken']),
  }
</script>

<style scoped>
  a {
    color: #000;
  }
</style>
