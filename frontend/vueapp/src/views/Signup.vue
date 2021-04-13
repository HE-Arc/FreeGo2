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
      v-model="password1"
      :error-messages="passwordErrors"
      :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
      :type="show1 ? 'text' : 'password'"
      label="Mot de passe"
      required
      @click:append="show1 = !show1"
      @input="$v.password1.$touch()"
      @blur="$v.password1.$touch()"
    ></v-text-field>
    
    <v-text-field
      v-model="password2"
      :error-messages="passwordErrors"
      :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
      :type="show2 ? 'text' : 'password'"
      label="Mot de passe"
      required
      @click:append="show2 = !show2"
      @input="$v.password2.$touch()"
      @blur="$v.password2.$touch()"
    ></v-text-field>

    <v-text-field
      v-model="email"
      :error-messages="emailErrors"
      label="E-mail"
      required
      @input="$v.email.$touch()"
      @blur="$v.email.$touch()"
    ></v-text-field>
    <v-btn
      class="mr-4"
      :disabled="submitStatus === 'PENDING'"
      color="Primary"
      @click="signup"
      :to="{ name:'signup'}"
    >
      Créer un compte
    </v-btn>
  </form>

</template>

<script>
  import { required, email } from 'vuelidate/lib/validators'
  import { getAPI } from '../axios-api'

  export default {
    name: 'signup',

    data () {
      return {
        username: '',
        password1: '',
        password2: '',
        email: '',
        submitStatus: null,
        show1: false,
        show2: false,
      }
    },

    validations: {
      username: {
        required,
      },
      password1: {
        required,
      },
      password2: {
        required,
      },
      email: {
        required,
        email,
      },
    },

    computed: { 
      usernameErrors () {
        const errors = []
        if (!this.$v.username.$dirty) return errors
        !this.$v.username.required && errors.push('Veuillez choisir votre nom d\'utilisateur')
        return errors
      },
      passwordErrors () {
        const errors = []
        if (!this.$v.password1.$dirty) return errors
        !this.$v.password1.required && errors.push('Veuillez entrer votre mot de passe')
        if (!this.$v.password2.$dirty) return errors
        !this.$v.password2.required && errors.push('Veuillez confirmer votre mot de passe')
        return errors
      },
      emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push('Veuillez entrer une adresse e-mail valide')
        !this.$v.email.required && errors.push('Veuillez entrer votre adresse e-mail')
        return errors
      },
    },

    methods: {
      signup(){
        this.$v.$touch()
        if (this.$v.$invalid) {
          this.submitStatus = 'ERROR'
        } else {
          this.submitStatus = 'PENDING'
          //Signup logic here
          getAPI.post('/register/', {
            username: this.username,
            password1: this.password1,
            password2: this.password2,
            email: this.email,
          })
          .then(() => {
            this.$store.dispatch('userLogin', {
              username: this.username,
              password: this.password1
            })
            this.$router.push({ name: 'home' })
          })
          .catch(err => {
            console.log(err)
          })
          .finally(() => {
            this.submitStatus = 'OK'
          })
        }
      }
    },
  }
</script>

<style>
</style>