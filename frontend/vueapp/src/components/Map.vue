<template>
  <div id="mapContainer"></div>
</template>

<script>
  import "leaflet/dist/leaflet.css";
  import L from "leaflet";
  import omnivore from "@mapbox/leaflet-omnivore"
  import { getAPI } from '../axios-api'

  export default {
    name: 'Map',

    components: {
    },

    data() {
      return {
        map: null,
        coordinates: {
          lat: 0,
          lng: 0,
        },
      }
    },

    created() {
      this.$getLocation({})
      .then(coordinates =>{
        this.coordinates = coordinates
        this.map.setView(this.coordinates, 10)
      })
      .catch(error => alert(error))
    },

    mounted() {
      this.map = L.map('mapContainer', 'mapbox.streets')
      L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(this.map)

      getAPI.get('/kmlfile/')
      .then(response => {
        omnivore.kml(response.data[0].kml_file).addTo(this.map)
      })
      .catch(err => {
        console.log(err)
      })
    },

    beforeDestroy() {
      if (this.map) {
        this.map.remove()
      }
    },
  }
</script>

<style scoped>
  #mapContainer {
    width: 100%;
    height: 75vh;
  }
</style>