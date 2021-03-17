<template>
    
  <form>
    <v-text-field
      v-model="username"
      :error-messages="usernameErrors"
      label="Nom d'utilisateur"
      required
      @input="$v.username.$touch()"
      @blur="$v.username.$touch()"
    ></v-text-field>
    
    <v-text-field
      v-model="password"
      :error-messages="passwordErrors"
      :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
      :type="show ? 'text' : 'password'"
      label="Mot de passe"
      required
      @click:append="show = !show"
      @input="$v.password.$touch()"
      @blur="$v.password.$touch()"
    ></v-text-field>
    <v-btn
      class="mr-4"
      :disabled="submitStatus === 'PENDING'"
      @click="login"
      color="primary"
    >
    Se connecter
    </v-btn>
    <p v-if="incorrectAuth">Nom d'utilisateur ou mot de passe incorrect - veuillez réessayer</p>
  </form>

</template>

<script>
  import { mapState } from 'vuex'
  import { required } from 'vuelidate/lib/validators'

  export default {
    name: 'login',

    components: {
    },

    data () {
      return {
        username: '',
        password: '',
        incorrectAuth: false,
        submitStatus: null,
        show: false,
      }
    },

    validations: {
      username: {
        required,
      },
      password: {
        required,
      },
    },

    computed: { 
      ...mapState(['accessToken']),
      usernameErrors () {
        const errors = []
        if (!this.$v.username.$dirty) return errors
        !this.$v.username.required && errors.push('Veuillez entrer votre nom d\'utilisateur')
        return errors
      },
      passwordErrors () {
        const errors = []
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.required && errors.push('Veuillez entrer votre mot de passe')
        return errors
      },
    },

    methods: {
      login() {
        this.$v.$touch()
        if (this.$v.$invalid) {
          this.submitStatus = 'ERROR'
        } else {
          this.submitStatus = 'PENDING'
          this.$store.dispatch('userLogin', {
            username: this.username,
            password: this.password
          })
          .then(() => {
            this.$router.push({ name: 'home' })
          })
          .catch(err => {
            console.log(err)
            this.incorrectAuth = true
          })
          .finally(() =>{
            this.submitStatus = 'OK'
          })
        }
      }
    },
  }
</script>

<style>

</style>