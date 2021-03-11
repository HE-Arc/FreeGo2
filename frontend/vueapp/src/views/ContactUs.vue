<template>
  <div>
    <Head/>
    <form>
      <v-col cols="12" md="4">
        <v-text-field
          v-model="subject"
          :error-messages="subjectErrors"
          :counter="50"
          label="Sujet"
          required
          @input="$v.subject.$touch()"
          @blur="$v.subject.$touch()"
        ></v-text-field>
        
        <v-text-field
          v-model="emailAddress"
          :error-messages="emailErrors"
          label="Votre adresse email"
          required
          @input="$v.emailAddress.$touch()"
          @blur="$v.emailAddress.$touch()"
        ></v-text-field>
        
        <v-textarea
          v-model="message"
          :error-messages="messageErrors"
          label="Message"
          required
          @change="$v.message.$touch()"
          @blur="$v.message.$touch()"
        ></v-textarea>
        <v-btn
          class="mr-4"
          :disabled="submitStatus === 'PENDING'"
          @click="submit"
          color="primary"
        >
          Envoyer
        </v-btn>
      </v-col>
      <p class="typo__p" v-if="submitStatus === 'OK'">Merci de votre message !</p>
      <p class="typo__p" v-if="submitStatus === 'ERROR'">Veuillez corriger les erreurs.</p>
      <p class="typo__p" v-if="submitStatus === 'PENDING'">Envoi...</p>
    </form>
    <Navbar/>
  </div>
</template>

<script>
  import Navbar from '../components/Navbar'
  import Head from '../components/Head'
  import { required, minLength, email } from 'vuelidate/lib/validators'

  export default {
    name: 'ContactUs',

    components: {
      Navbar,
      Head,
    },

    data () {
      return {
        subject: '',
        emailAddress: '',
        message: '',
        submitStatus: null,
      }
    },

    validations: {
      subject: {
        required,
        minLength: minLength(4)
      },
      emailAddress: {
        required,
        email
      },
      message: {
        required
      },
    },

    computed: {
      subjectErrors () {
        const errors = []
        if (!this.$v.subject.$dirty) return errors
        !this.$v.subject.minLength && errors.push('Le sujet doit faire au moins 4 charactères.')
        !this.$v.subject.required && errors.push('Le sujet est obligatoire.')
        return errors
      },
      emailErrors () {
        const errors = []
        if (!this.$v.emailAddress.$dirty) return errors
        !this.$v.emailAddress.email && errors.push('Doit être une adresse email valide.')
        !this.$v.emailAddress.required && errors.push('Une adresse email est obligatoire.')
        return errors
      },
      messageErrors () {
        const errors = []
        if (!this.$v.message.$dirty) return errors
        !this.$v.message.required && errors.push('Un message est obligatoire.')
        return errors
      },
    },

    methods: {
      submit() {
        this.$v.$touch()
        if (this.$v.$invalid) {
          this.submitStatus = 'ERROR'
        } else {
          // TODO: submit logic here
          this.submitStatus = 'PENDING'
          setTimeout(() => {
            this.submitStatus = 'OK'
          }, 500)
        }
      },
    },
  }
</script>

<style scoped>

</style>