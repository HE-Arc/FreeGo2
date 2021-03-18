<template>
  <div>
    <v-row v-for="i in menusAmount" :key="i">
      <v-col>
        <v-text-field :disabled="i > menusAmount" dense label="Menu" :counter="20" :error-messages="menusErrors" v-on:change="addMenu($event, i)" @input="$v.menus.$touch()" @blur="$v.menus.$touch()"></v-text-field>
      </v-col>
      <v-col>
        <v-text-field :disabled="!menus[i-1]" dense label="Allergènes" placeholder="lactose, noix" v-on:change="addAllergens($event, i)"></v-text-field>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  import { maxLength } from 'vuelidate/lib/validators'

  export default {
    name: 'AddMenu',

    data: () => ({
      menusAmount: 1,
      menus: [],
      allergens: [],
    }),

    computed: {
      menusErrors () {
        const errors = []
        if (!this.$v.menus.$dirty) return errors
        !this.$v.menus.maxLength && errors.push('Le nom du menu est trop long !')
        return errors
      },
    },

    validations: {
      menus: {
        maxLength: maxLength(20),
      },
    },

    methods: {
      addMenu(menu, i) {
        i -= 1;
        // If menu is not an empty string, add it to the menus array. Otherwise, put null instead
        this.menus[i] = (menu ? menu : this.menus[i] = null)
        this.checkMenusIntegrity()
        console.log(this.menus)
      },
      checkMenusIntegrity() {
        // Delete null entries at the end of the menus array
        while(this.menus[this.menus.length - 1] == null && this.menus.length > 0){
          this.menus.pop()
        }
        // Then updates the amount of menu fields to display
        this.menusAmount = this.menus.length + 1
      },
      addAllergens(allergens, i) {
        i -= 1
        this.allergens[i] = allergens
      },
    }
  }
</script>

<style scoped>
</style>
