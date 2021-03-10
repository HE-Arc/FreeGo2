<template>

  <v-card class="mx-auto" max-width="344" :to="{ name:'fridge', params: { fridgeId: fridge.id }}" exact>

    <v-card-title>
      {{ fridge.name }}
    </v-card-title>
    
    <v-card-subtitle>
      {{ fridge.manager_description }}
    </v-card-subtitle>

    <v-divider></v-divider>
  </v-card>

</template>

<script>
  export default {
    name: 'FridgeCard',
    props: ['fridge']
  }
</script>

<style scoped>
</style>