<template>
  <div>
    <h3>{{ fridge.name }}</h3>
    <v-btn color="primary" :to="{ name:'fridge', params: { fridgeId: fridge.id }}" exact>
      Voir le Free Go
    </v-btn>
  </div>
</template>

<script>
  export default {
    name: 'Popup',

    props: ['fridge'],
  }
</script>

<style scoped>
</style>