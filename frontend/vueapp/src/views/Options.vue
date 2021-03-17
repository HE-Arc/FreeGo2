<template>
  <div>
    <v-row>
      <OptionsMenu/>
    </v-row>
    <v-row>
      <SocialMediasMenu/>
    </v-row>
  </div>
</template>

<script>
  import OptionsMenu from '../components/OptionsMenu'
  import SocialMediasMenu from '../components/SocialMediasMenu'

  export default {
    name: 'Options',
    
    components: {
      OptionsMenu,
      SocialMediasMenu,
    },
  }
</script>

<style scoped>
</style>