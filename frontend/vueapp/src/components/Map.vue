<template>
  <div style="height: 75vh; width: 100%">
    <l-map
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: 100%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-geo-json
        :geojson="geojson"
      />
    </l-map>
  </div>
</template>

<script>
  import { latLng } from "leaflet"
  import { LMap, LTileLayer, LGeoJson } from "vue2-leaflet"
  import { getAPI } from '../axios-api'

  export default {
    name: 'Map',

    components: {
      LMap,
      LTileLayer,
      LGeoJson,
    },

    data() {
      return {
        loading: false,
        zoom: 13,
        center: latLng(0, 0),
        geojson: null,
        fillColor: "#e4ce7f",
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution:
          '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        currentZoom: 11.5,
        currentCenter: latLng(0, 0),
        mapOptions: {
          zoomSnap: 0.5
        },
        }
    },

    async created() {
      this.$getLocation({})
      .then(coordinates =>{
        this.center = coordinates
      })
      .catch(error => alert(error))
    },
    
    methods: {
      zoomUpdate(zoom) {
        this.currentZoom = zoom
      },
      centerUpdate(center) {
        this.currentCenter = center
      },
    },

    mounted() {
      this.loading = true
      getAPI.get('/kmlfile/')
      .then(response => {
        console.log(response.data[0].geojson_file)
        this.geojson = JSON.parse(response.data[0].geojson_file)
        this.loading = false
      })
      .catch(err => {
        console.log(err)
      })
    },
  }
</script>

<style scoped>
</style>