<template>
  <div>
    <v-row>
      <OptionsMenu/>
    </v-row>
    <v-row>
      <SocialMediasMenu/>
    </v-row>
    <v-row>
      <Sponsors/>
    </v-row>
  </div>
</template>

<script>
  import OptionsMenu from '../components/OptionsMenu'
  import SocialMediasMenu from '../components/SocialMediasMenu'
  import Sponsors from '../components/Sponsors'

  export default {
    name: 'Options',
    
    components: {
      OptionsMenu,
      SocialMediasMenu,
      Sponsors,
    },
  }
</script>

<style scoped>
</style>