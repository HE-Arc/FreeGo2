<template>
    
  <form>
    <!-- TODO: Get manager's fridge through APIData and fill the form with already existing data -->
    <h1>{{ APIData.name }}</h1>

    <v-file-input
      accept="image/png, image/jpeg, image/bmp"
      placeholder="Photos de votre Free Go"
      prepend-icon="mdi-camera"
      label="Photos"
      small-chips
      multiple
      clearable
      @change="previewImages"
    ></v-file-input>

    <v-img :src="imageUrl" style="border: 1px dashed #ccc; height: 120px; width: 90px;" />

    <AddMenu/>
      
    <v-textarea
      v-model="description"
      label="Panneaux d'affichage"
      :error-messages="descriptionErrors"
      :counter="300"
      clearable
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
  import AddMenu from '../components/AddMenu'

  export default {
    name: 'ManageFridge',

    components: {
      AddMenu,
    },

    data () {
      return {
        images: null,
        imageUrl: '',
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
        maxLength: maxLength(20),
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
          /* getAPI.put('/fridge/'.concat().concat('/'), {
          })
          .then(response => {
            console.log(response)
          })
          .catch(err => {
            console.log(err)
          }) */

          this.submitStatus = 'PENDING'
          setTimeout(() => {
            this.submitStatus = 'OK'
          }, 500)
        }
      },
      createImage(files) {
        const reader = new FileReader();
        
        files.forEach(file => {
          reader.onload = (e) => {
            this.imageUrl=e.target.result;
          };
          reader.readAsDataURL(file);
        });
      },
      previewImages(files) {
        if (!files) {
          return;
        }
        this.createImage(files);
      },
    },
  }
</script>

<style scoped>
</style>