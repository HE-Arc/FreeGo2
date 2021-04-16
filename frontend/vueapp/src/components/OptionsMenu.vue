<template>

  <v-col>
    <v-list>
      <v-list-item link :to="{ name:'donations' }" exact>
        <v-list-item-content>
          <v-list-item-title>Donations</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item link :to="{ name:'contactUs' }" exact>
        <v-list-item-content>
          <v-list-item-title>Nous contacter</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item v-if="select">
        <!-- TODO: ManageFridge should only be available to Manager role -->
        <v-list-item-content>
          <span>
            <v-select
              v-model="select"
              :items="fridges"
              item-text="fridge_name"
              label="Choisir un Free Go"
              return-object
              single-line
            ></v-select>
            <v-btn link :to="{ name:'manageFridge', params: { fridgeId: select.fridge }}" exact>Gérer</v-btn>
          </span>
        </v-list-item-content>
      </v-list-item>

      <v-list-item v-if="accessToken==null" link :to="{ name:'login' }" exact>
        <v-list-item-content>
          <v-list-item-title>Se connecter</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item v-else link :to="{ name:'logout' }" exact>
        <v-list-item-content>
          <v-list-item-title>Se déconnecter</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-col>

</template>

<script>
  import { getAPI } from '../axios-api'
  import { mapState } from 'vuex'

  export default {
    name: 'OptionsMenu',
    
    computed: mapState(['accessToken']),

    data () {
      return {
        select: null,
        fridges: [],
      }
    },

    created() {
      if(this.$store.state.accessToken){
        getAPI.get('/manager/', {
          params: {
            user: this.$store.state.userId
          },
          headers: {
            'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('token')).access}`
          },
        })
        .then(response => {
          response.data.forEach(fridge => this.fridges.push(fridge))
          this.select = this.fridges[0]
        })
        .catch(err => {
          console.log(err)
        })
      }
    }
  }
</script>

<style scoped>
</style>
