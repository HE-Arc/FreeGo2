<template>

  <v-row>
    <v-col>
      <v-card :to="{ name:'fridge', params: { fridgeId: fridge.id }}" exact>
        <v-card-title>
          {{ fridge.name }}
        </v-card-title>
        
        <v-card-subtitle>
          {{ fridge.manager_description }}
        </v-card-subtitle>
      </v-card>
    </v-col>
  </v-row>
  
</template>

<script>
  export default {
    name: 'FridgeCard',

    props: ['fridge'],
  }
</script>

<style scoped>
</style>