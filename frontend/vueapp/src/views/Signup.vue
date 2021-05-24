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
    <v-btn
      class="mr-4"
      :disabled="submitStatus === 'PENDING' || $v.$invalid"
      color="Primary"
      @click="signup"
      :to="{ name:'signup'}"
    >
      Créer un compte
    </v-btn>
  </form>

</template>

<script>
  import { required, minLength } from 'vuelidate/lib/validators'
  import { getAPI } from '../axios-api'

  export default {
    name: 'signup',

    data () {
      return {
        username: '',
        password1: '',
        password2: '',
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
        minLength: minLength(8),
        containsUppercase: function(value) {
          return /[A-Z]/.test(value)
        },
        containsLowercase: function(value) {
          return /[a-z]/.test(value)
        },
        containsNumber: function(value) {
          return /[0-9]/.test(value)
        },
        containsSpecial: function(value) {
          return /[#?!@$%^&*-]/.test(value)
        }
      },
      password2: {
        required,
        matchPassword1: function(value) {
          return this.password1 == value
        }
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
        !this.$v.password1.minLength && errors.push('Le mot de passe doit faire au minimum 8 caractères')
        !this.$v.password1.containsUppercase && errors.push('Le mot de passe doit comprendre au moins une majuscule')
        !this.$v.password1.containsLowercase && errors.push('Le mot de passe doit comprendre au moins une minuscule')
        !this.$v.password1.containsNumber && errors.push('Le mot de passe doit comprendre au moins un chiffre')
        !this.$v.password1.containsSpecial && errors.push('Le mot de passe doit comprendre au moins un caractère spécial (#?!@$%^&*-)')
        if (!this.$v.password2.$dirty) return errors
        !this.$v.password2.required && errors.push('Veuillez confirmer votre mot de passe')
        !this.$v.password2.matchPassword1 && errors.push('Le mot de passe ne correspond pas au premier')
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
          
          getAPI.post('/register/', {
            username: this.username,
            password1: this.password1,
            password2: this.password2,
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