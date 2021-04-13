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

  export default {
    name: 'signup',

    data () {
      return {
        username: '',
        password: '',
        email: '',
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
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.required && errors.push('Veuillez entrer votre mot de passe')
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

          
        }
      }
    },
  }
</script>

<style>
</style>