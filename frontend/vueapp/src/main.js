import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'
import store from './store'
import vuetify from './plugins/vuetify';
import './registerServiceWorker'
import VueGeolocation from 'vue-browser-geolocation'
import 'leaflet/dist/leaflet.css'
import L from "leaflet"

Vue.config.productionTip = false
Vue.use(VueGeolocation)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: 'login' })
    } else {
      next()
    }
  } else {
    next()
  }
})

delete L.Icon.Default.prototype._getIconUrl
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
})