<template>
  <div class="google-map" ref="googleMap">
    <!-- <iframe src="https://www.google.com/maps/d/embed?mid=1hc3fe23eojoXxayFh9kONc6v6ezx558u" width="100%" height="400px"></iframe> -->
    <GmapMap 
      :center="coordinates" 
      :zoom="10" 
      style="width:100%; height:400px;"
      ref="mapRef"
    ></GmapMap>
  </div>
</template>

<script>
  export default {
    name: 'Map',

    data() {
      return {
        map: null,
        coordinates: {
          lat: 0,
          lng: 0,
        }
      }
    },

    created() {
      this.$getLocation({})
      .then(coordinates =>{
        this.coordinates = coordinates
      })
      .catch(error => alert(error))
    },

    mounted() {
      this.$refs.mapRef.$mapPromise.then(map => this.map = map)
    },
  }
</script>

<style scoped>
</style>