<template>
    
  <form>
    <!-- TODO: Get manager's fridge through APIData -->
    <h1>{{ APIData.name }}</h1>

    <v-textarea
      v-model="menus"
      label="Menus"
      :error-messages="menusErrors"
      :counter="300"
      @input="$v.menus.$touch()"
      @blur="$v.menus.$touch()"
    ></v-textarea>
      
    <v-textarea
      v-model="description"
      label="Panneaux d'affichage"
      :error-messages="descriptionErrors"
      :counter="300"
      @input="$v.description.$touch()"
      @blur="$v.description.$touch()"
    ></v-textarea>

    <v-btn
      class="mr-4"
      :disabled="submitStatus === 'PENDING'"
      @click="submit"
      color="primary"
    >
      Enregistrer
    </v-btn>
    <p class="typo__p" v-if="submitStatus === 'OK'">Changements enregistrés !</p>
    <p class="typo__p" v-if="submitStatus === 'ERROR'">Veuillez corriger les erreurs.</p>
    <p class="typo__p" v-if="submitStatus === 'PENDING'">Envoi...</p>
  </form>

</template>

<script>
  import { getAPI } from '../axios-api'
  import { mapState } from 'vuex'
  import { maxLength } from 'vuelidate/lib/validators'

  export default {
    name: 'ContactUs',

    components: {
    },

    data () {
      return {
        // TODO: fill menus and description with APIData
        images: null,
        menus: '',
        description: '',
        submitStatus: null,
      }
    },

    computed: {
      ...mapState(['APIData']),
      descriptionErrors () {
        const errors = []
        if (!this.$v.description.$dirty) return errors
        !this.$v.description.maxLength && errors.push('Le texte est trop long !')
        return errors
      },
      menusErrors () {
        const errors = []
        if (!this.$v.menus.$dirty) return errors
        !this.$v.menus.maxLength && errors.push('Le texte des menus est trop long !')
        return errors
      },
    },

    created () {
      getAPI.get(((this.$route.params.fridgeId) ? '/fridge/'.concat(this.$route.params.fridgeId) : '/fridge/'), )
      .then(response => {
        this.$store.state.APIData = response.data
      })
      .catch(err => {
        console.log(err)
      })
    },

    validations: {
      menus: {
        maxLength: maxLength(300),
      },
      description: {
        maxLength: maxLength(300),
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