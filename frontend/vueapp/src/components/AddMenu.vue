<template>
  <div v-if="menusAmount">
    <v-row v-for="i in menusAmount" :key="i">
      <v-col>
        <v-text-field 
          v-model="menus[i-1]"
          :disabled="i > menusAmount" 
          dense 
          label="Menu" 
          :counter="20" 
          :error-messages="menusErrors" 
          v-on:change="addMenu($event, i)" 
          @input="$v.menusJson.$touch()" 
          @blur="$v.menusJson.$touch()"
        ></v-text-field>
      </v-col>
      <v-col>
        <v-text-field 
          v-model="allergens[i-1]"
          :disabled="!menusJson[i-1]" 
          dense label="Allergènes" 
          placeholder="lactose, noix..." 
          v-on:change="addAllergens($event, i)"
        ></v-text-field>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  import { maxLength } from 'vuelidate/lib/validators'

  export default {
    name: 'AddMenu',

    data: () => ({
      menusAmount: null,
      menus: [],
      allergens: [],
    }),

    props: {
      menusJson: Array
    },

    computed: {
      menusErrors () {
        const errors = []
        if (!this.$v.menusJson.$dirty) return errors
        !this.$v.menusJson.maxLength && errors.push('Le nom du menu est trop long !')
        return errors
      },
    },

    validations: {
      menusJson: {
        maxLength: maxLength(20),
      },
    },

    created() {
      this.menusAmount = this.menusJson.length + 1
      this.menusJson.forEach(menu => {
        this.menus.push(menu.name)
        let menuAllergens = []
        menu.children.forEach(allergen => {
          menuAllergens.push(allergen.name)
        })
        this.allergens.push(menuAllergens)
      })
    },

    methods: {
      addMenu(menusJson, i) {
        i -= 1
        // If menu is not an empty string, add it to the menus array. Otherwise, put null instead
        this.menusJson[i] = (menusJson ? menusJson : this.menusJson[i] = null)
        this.checkMenusIntegrity()
      },
      checkMenusIntegrity() {
        // Delete null entries at the end of the menus array
        while(this.menusJson[this.menusJson.length - 1] == null && this.menusJson.length > 0){
          this.menusJson.pop()
        }
        // Then updates the amount of menu fields to display
        this.menusAmount = this.menusJson.length + 1
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
