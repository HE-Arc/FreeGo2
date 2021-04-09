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
    <Popup v-bind:fridge="fridge" v-show=showPopup ref='popup'/>
  </l-map>
</template>

<script>
  import { latLng } from "leaflet"
  import { LMap, LTileLayer, LGeoJson } from "vue2-leaflet"
  import { getAPI } from '../axios-api'
  import Popup from '../components/Popup'

  export default {
    name: 'Map',

    components: {
      LMap,
      LTileLayer,
      LGeoJson,
      Popup
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
        showPopup: false,
        fridge: {
          name: 'name',
          id: '1'
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
        return (feature, marker) => {
          if (feature.geometry.type == "Point") {
            marker.bindPopup(
              () => this.$refs.popup.$el,
              {
                maxWidth: "auto",
              }
            )
            marker.on('click', () => {
              getAPI.get('/fridge/', {
                params: {
                  name: feature.properties.name
                }
              })
              .then(response => {
                this.fridge.name = response.data[0].name
                this.fridge.id = response.data[0].id
              })
              .catch(err => {
                console.log(err)
              })
              this.showPopup = true
            })
          }
        }
      }
    },

    async created() {
      this.$getLocation({})
      .then(coordinates => {
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