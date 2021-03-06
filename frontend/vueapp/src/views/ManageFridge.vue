<template>
    
  <v-card>
    <v-card-title>{{ fridge }}</v-card-title>
    <v-card-text>
      <form>

        <v-row>
          <v-col cols="12" align="center" justify="space-around">
            <v-file-input
              accept="image/png, image/jpeg, image/bmp"
              prepend-icon='mdi-camera'
              label="Photos"
              small-chips
              multiple
              clearable
              @change="previewImages"
            ></v-file-input>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            cols="3"
            v-for="i in oldImagesAmount"
            :key="i"
          >
            <v-card
              @click="addToDelete(i-1)"
            >
              <v-img
                :src="oldImages[i-1]"
                :gradient="oldImagesFlag[i-1] ? '' : 'to top, rgba(0,0,0,.8), rgba(0,0,0,.8)'"
              />
            </v-card>
          </v-col>

          <v-col
            cols="3"
            v-for="i in imagesAmount"
            :key="'o'+i"
          >
            <v-card
              @click="removeFromPost(i-1)"
            >
              <v-img
                :src="images[i-1]" 
                :gradient="imagesFlag[i-1] ? '' : 'to top, rgba(0,0,0,.8), rgba(0,0,0,.8)'"
              />
            </v-card>
          </v-col>
        </v-row>

        <AddMenu v-if="menus" :menus="menus" :allergens="allergens" :menusAmount="menusAmount"></AddMenu>
          
        <v-textarea
          v-model="description"
          label="Panneaux d'affichage"
          :error-messages="descriptionErrors"
          :counter="300"
          hint="Informez les utilisateurs des horaires spéciaux !"
          clearable
          multi-line
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
  import Vue from 'vue'
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
        oldImagesAmount: 0,
        oldImages: [],
        oldImagesId: [],
        oldImagesIdToDelete: [],
        oldImagesFlag: [],
        imagesAmount: 0,
        images: [],
        imagesToPost: [],
        imagesFlag: [],
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
        this.$nextTick().then(() => {
          this.fridge = response.data.name
          this.fridgeId = response.data.id
          this.menusJson = response.data.menu_list.items
          this.description = response.data.manager_description
          response.data.pictures.forEach(picture => {
            this.oldImages.push(picture.image)
            this.oldImagesId.push(picture.id)
            this.oldImagesFlag.push(true)
          })
          this.oldImagesAmount = this.oldImages.length

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
        this.menusAmount = this.menus.length + 1
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
              menu_list: this.createMenusJSON()
            },
            {
              headers: {
                'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('token')).access}`
              },
            }
          )
          .then(() => {
            getAPI.get('/favorite/', {
              params:{
                fridge: this.fridgeId,
              },
            })
            .then(response => {

              for(let i=0; i < response.data.length; i++){
                getAPI.post('/notification/', {
                  fridge: this.fridgeId,
                  user: response.data[i].user,
                },
                {
                  headers: {
                    'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('token')).access}`
                  },
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

          for(let i = 0; i < this.imagesToPost.length; i++){
            const formData = new FormData()
            formData.append("image", this.imagesToPost[i])
            formData.append("fridge", this.fridgeId)
            getAPI.post('/picture/', formData, {
              headers: {
                'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('token')).access}`,
                'Content-Type': 'multipart/form-data',
              }
            })
            .catch(err => {
              console.log(err)
            })
          }

          for(let i = 0; i < this.oldImagesIdToDelete.length; i++){
            getAPI.delete('/picture/'.concat(this.oldImagesIdToDelete[i]).concat('/'), {
              headers: {
                'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('token')).access}`
              }
            })
            .catch(err => {
              console.log(err)
            })
          }

          this.submitStatus = 'PENDING'
          setTimeout(() => {
            this.submitStatus = 'OK'
            this.$router.push({ path : '/fridge/'.concat(this.fridgeId) });
          }, 500)

        }
      },

      addToDelete(index) {
        if(!this.oldImagesIdToDelete.includes(this.oldImagesId[index])) {
          this.oldImagesIdToDelete.push(this.oldImagesId[index])
          Vue.set(this.oldImagesFlag, index, false)
        }
        else {
          for(let i = 0; i < this.oldImagesIdToDelete.length; i++){
            if (this.oldImagesIdToDelete[i] === this.oldImagesId[index]) {
              this.oldImagesIdToDelete.splice(i, 1)
              i--
            }
          }
          Vue.set(this.oldImagesFlag, index, true)
        }
      },

      removeFromPost(index) {
        if(this.imagesToPost.includes(this.images[index])) {
          for(let i = 0; i < this.imagesToPost.length; i++){
            if (this.imagesToPost[i] === this.images[index]) {
              this.imagesToPost.splice(i, 1)
              i--
            }
          }
          Vue.set(this.imagesFlag, index, false)
        }
        else {
          this.imagesToPost.push(this.images[index])
          Vue.set(this.imagesFlag, index, true)
        }
      },

      createImage(files) {
        files.forEach(file => {
          const reader = new FileReader()
          reader.onload = (e) => {
            this.images.push(e.target.result)
            this.imagesToPost.push(e.target.result)
            this.imagesFlag.push(true)
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