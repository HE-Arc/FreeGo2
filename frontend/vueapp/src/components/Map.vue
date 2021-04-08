<template>
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
      :options="options"
      :options-style="styleFunction"
    />
  </l-map>
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
      LGeoJson
    },

    data() {
      return {
        loading: false,
        zoom: 13,
        center: latLng(0, 0),
        geojson: null,
        fillColor: "#d6ffff",
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        currentZoom: 13,
        currentCenter: latLng(0, 0),
        mapOptions: {
          zoomSnap: 0.5
        },
      }
    },

    computed: {
      options() {
        return {
          onEachFeature: this.onEachFeatureFunction
        }
      },

      styleFunction() {
        const fillColor = this.fillColor 
        return () => {
          return {
            weight: 2,
            color: "#0094ad",
            opacity: 1,
            fillColor: fillColor,
            fillOpacity: 0.3
          }
        }
      },

      onEachFeatureFunction() {
        return (feature, layer) => {
          if (feature.geometry.type == "Point") {

            getAPI.get('/fridge/', {
              params: {
                name: feature.properties.name
              }
            })
            .then(response => {
              layer.bindPopup(
                "<h3>" +
                feature.properties.name +
                "</h3><a href=\"http://localhost:8080/fridge/" +
                response.data[0].id +
                "\">Voir le Free Go</a>",
                { permanent: false, sticky: true }
              )
            })
            .catch(err => {
              console.log(err)
            })
          }
        }
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