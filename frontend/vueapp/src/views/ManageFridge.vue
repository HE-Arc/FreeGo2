<template>
    
  <v-card>
    <v-card-title>{{ fridge }}</v-card-title>
    <v-card-text>
      <form>

        <v-file-input
          accept="image/png, image/jpeg, image/bmp"
          placeholder="Photos du Free Go"
          prepend-icon="mdi-camera"
          label="Photos"
          small-chips
          multiple
          clearable
          @change="previewImages"
        ></v-file-input>

        <v-img 
          v-for="i in imagesAmount"
          :key="i"
          :src="imagesUrl[i-1]" 
          style="border: 1px dashed #ccc; height: 120px; width: 90px;" 
        />

        <AddMenu v-if="menus" :menus="menus" :allergens="allergens" :menusAmount="menusAmount"></AddMenu>
          
        <v-textarea
          v-model="description"
          label="Panneaux d'affichage"
          :error-messages="descriptionErrors"
          :counter="300"
          hint="Informez les utilisateurs des horaires spéciaux !"
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
    </v-card-text>
  </v-card>

</template>

<script>
  import { getAPI } from '../axios-api'
  import { maxLength } from 'vuelidate/lib/validators'
  import AddMenu from '../components/AddMenu'

  export default {
    name: 'ManageFridge',

    components: {
      AddMenu,
    },

    data() {
      return {
        fridge: '',
        fridgeId: null,
        imagesAmount: null,
        imagesUrl: [],
        menusJson: null,
        menusAmount: null,
        menus: [],
        allergens: [],
        description: '',
        submitStatus: null,
      }
    },

    computed: {
      descriptionErrors () {
        const errors = []
        if (!this.$v.description.$dirty) return errors
        !this.$v.description.maxLength && errors.push('Le texte est trop long !')
        return errors
      },
    },

    created() {
      getAPI.get('/fridge/'.concat(this.$route.params.fridgeId).concat('/'))
      .then(response => {
        this.fridge = response.data.name
        this.fridgeId = response.data.id
        this.menusJson = response.data.menu_list.items
        this.description = response.data.manager_description
        response.data.pictures.forEach(picture => {
          this.imagesUrl.push(picture.image)
        })
        this.imagesAmount = this.imagesUrl.length

        this.menusJson.forEach(menu => {
          this.menus.push(menu.name)
          let menuAllergens = []
          if(menu.children) {
            menu.children.forEach(allergen => {
              menuAllergens.push(allergen.name)
            })
          }
          this.allergens.push(menuAllergens)
        })
        this.menusAmount = this.menusJson.length + 1
      })
      .catch(err => {
        console.log(err)
      })      
    },

    validations: {
      description: {
        maxLength: maxLength(300),
      },
    },

    methods: {
      createMenusJSON () {
        // Create a json object to use for our menus and allergens
        let menusText = '{"items": ['

        let i = 0
        this.menus.forEach(menu => {
          menusText += '{"name": "' + menu + '"'
          if(this.allergens[i].toString() !== "") {
            menusText += ', "children": ['
            let allergenIndex = 0
            let allergenList = this.allergens[i].toString().split(",")
            allergenList.forEach(allergen => {
              menusText += '{"name": "' + allergen + '"}'
              if(allergenIndex < allergenList.length-1){
                menusText += ','
              }
              allergenIndex++
            })
            menusText += ']'
          }
          menusText += '}'
          if(i < this.menusAmount-2) {
              menusText += ','
            }
          i++
        })
        menusText += ']}'
        return JSON.parse(menusText)
      },

      submit() {

        this.$v.$touch()
        if (this.$v.$invalid) {
          this.submitStatus = 'ERROR'
        } else {
          getAPI.patch('/fridge/'.concat(this.fridgeId).concat('/'), {
              manager_description: this.description,
              menu_list: this.createMenusJSON(),
          })
          .then(() => {

            getAPI.get('/favorite/', {
              params:{
                fridge: this.fridgeId,
              }
            })
            .then(response => {

              for(let i=0; i < response.data.length; i++){
                getAPI.post('/notification/', {
                  fridge: this.fridgeId,
                  user: response.data[i].user,
                })
                .catch(err => {
                  console.log(err)
                })
              }
              
            })
            .catch(err => {
              console.log(err)
            })

          })
          .catch(err => {
            console.log(err)
          })

          // TODO: Submit pictures
          for(let i = 0; i < this.imagesUrl.length; i++){
            const formData = new FormData()
            console.log(this.imagesUrl[i])
            formData.append("image", this.imagesUrl[i])
            formData.append("fridge", this.fridgeId)
            getAPI.post('/picture/', formData, {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            })
            .then(response => {
              console.log(response)
            })
            .catch(err => {
              console.log(err)
            })
          }

          this.submitStatus = 'PENDING'
          setTimeout(() => {
            this.submitStatus = 'OK'
          }, 500)
        }
      },

      createImage(files) {
        files.forEach(file => {
          const reader = new FileReader()
          reader.onload = (e) => {
            this.imagesUrl.push(e.target.result)
            this.imagesAmount++
          }
          reader.readAsDataURL(file)
        })
      },
      
      previewImages(files) {
        if (!files) {
          return;
        }
        this.createImage(files)
      },
    },
  }
</script>

<style scoped>
</style>