<template>

  <v-row>
    <v-col>
      <v-card :to="{ name:'fridge', params: { fridgeId: fridge }}" exact>
        <v-card-title>
          {{ APIData.name }}
        </v-card-title>
        
        <v-card-subtitle>
          {{ APIData.manager_description }}
        </v-card-subtitle>
      </v-card>
    </v-col>
  </v-row>
  
</template>

<script>
  import { getAPI } from '../axios-api'

  export default {
    name: 'FridgeCard',

    props: ['fridge'],
    
    data: () => ({
      APIData: {},
    }),

    created() {
      getAPI.get('/fridge/'.concat(this.fridge).concat('/'))
      .then(response => {
        this.APIData = response.data
      })
      .catch(err => {
        console.log(err)
      })
    },
  }
</script>

<style scoped>
</style>