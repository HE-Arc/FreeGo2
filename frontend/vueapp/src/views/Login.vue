<template>
  <div class="container text-dark">
    <div class="row justify-content-md-center">
      <div class="col-md-5 p-3 login justify-content-md-center">
        <h1 class="h3 mb-3 font-weight-normal text-center">S'enregistrer</h1>
        <p v-if="incorrectAuth">Nom d'utilisateur ou mot de passe incorrect - veuillez réessayer</p>
        <form v-on:submit.prevent="login">
          <div class="form-group">
            <input type="text" name="username" id="user" v-model="username" class="form-control" placeholder="Nom d'utilisateur">
          </div>
          <div class="form-group">
            <input type="password" name="password" id="pass" v-model="password" class="form-control" placeholder="Mot de passe">
          </div>
          <button class="btn btn-lg btn-primary btn-block">Se connecter</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'login',
  data () {
    return {
      username: '',
      password: '',
      incorrectAuth: false,
    }
  },
  computed: mapState(['accessToken']),
  methods: {
    login() {
      this.$store.dispatch('userLogin', {
        username: this.username,
        password: this.password
      })
      .then(() => {
        this.$router.push({ name: 'fridge' })
      })
      .catch(err => {
        console.log(err)
        this.incorrectAuth = true
      })
    }
  }
}
</script>

<style>

</style>