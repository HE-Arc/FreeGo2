<template>
  <v-card v-if="fridgeData">
    
    <v-card-title>
      <v-btn icon @click="favoriteClick"  v-if="accessToken!=null">
        <v-icon color="info" large>{{ isFavorite ? 'mdi-star' : 'mdi-star-outline' }}</v-icon>
      </v-btn>
      {{ fridgeData.name }}
    </v-card-title>
    <v-card-text><div v-for="(text, index) in fridgeData.my_maps_description.split('\\n')" :key="index">{{ text }}</div></v-card-text>
    <v-card-text><div v-for="(text, index) in fridgeData.manager_description.split('\\n')" :key="index">{{ text }}</div></v-card-text>

    <v-carousel>
      <v-carousel-item v-for="picture in fridgeData.pictures" :key=picture.image>
        <v-img v-bind:src="picture.image" :aspect-ratio="3/4"></v-img>
      </v-carousel-item>
    </v-carousel>

    <v-treeview dense :items="fridgeData.menu_list.items"></v-treeview>
  </v-card>
</template>

<script>
  import { getAPI } from '../axios-api'
  import { mapState } from 'vuex'

  export default {
    name: 'Fridge',

    components: {

    },
    
    data: () => ({
      favoriteId: null,
      isFavorite: null,
      fridgeData: false,
    }),

    computed: {
      ...mapState(['accessToken']),
    },

    created () {
      // TODO: Perform concurrent requests instead ?
      getAPI.get('/fridge/'.concat(this.$route.params.fridgeId).concat('/'))
      .then(response => {
        this.$nextTick().then(() => {
          this.fridgeData = response.data

          getAPI.get('/favorite/', {
            params: {
              user: this.$store.state.userId,
              fridge: this.fridgeData.id
            },
          })
          .then(response => {
            if (response.data[0]){
              this.isFavorite = true
              this.favoriteId = response.data[0].id
            }
          })
          .catch(err => {
            console.log(err)
          })

        })
        .catch(err => {
          console.log(err)
        })
      })
    },

    methods: {
      favoriteClick() {
        this.$nextTick().then(() => {
          if (this.favoriteId) {
            getAPI.delete('/favorite/'.concat(this.favoriteId).concat('/'), {
              headers: {
                'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('token')).access}`
              },
            })
            .then(() => {
              this.isFavorite = false
              this.favoriteId = null
            })
            .catch(err => {
              console.log(err)
            })
          }
          else {
            getAPI.post('/favorite/', {
                user: this.$store.state.userId,
                fridge: this.fridgeData.id
              },
              {
                headers: {
                  'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('token')).access}`
                }
              }
            )
            .then(response => {
              this.isFavorite = true
              this.favoriteId = response.data
            })
            .catch(err => {
              console.log(err)
            })
          }
        })
      }
    },
  }
</script>

<style scoped>
</style>