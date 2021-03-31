<template>
  <v-row v-if="fridgesAmount">
    <v-col>
      <v-card v-for="i in fridgesAmount" :key="i" link :to="{name:'fridge', params: { fridgeId: fridgesId[i-1] }}">
        <v-card-title>{{ fridgesName[i-1] }}</v-card-title>
        <v-card-text>{{ fridgesManagerDescription[i-1] }}</v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
  import { getAPI } from '../axios-api'

  export default {
    name: 'Notifications',

    components: {
    },

    data() {
      return {
        fridgesName: [],
        fridgesId: [],
        fridgesManagerDescription: [],
        fridgesAmount: null,
      }
    },

    created() {
      getAPI.get('/notification/', {
        params: {
          user: this.$store.state.userId,
        }
      })
      .then(response => {
        response.data.forEach(element => {
          getAPI.get('/fridge/'.concat(element.fridge).concat('/'))
          .then(response => {
            this.fridgesName.push(response.data.name)
            this.fridgesId.push(response.data.id)
            this.fridgesManagerDescription.push(response.data.manager_description)
            this.fridgesAmount = this.fridgesId.length
          })
          .catch(err => {
            console.log(err)
          })
        })
      })
      .catch(err => {
        console.log(err)
      })
    },
  }
</script>

<style scoped>

</style>
