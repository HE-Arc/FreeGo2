import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from './axios-api'

Vue.use(Vuex)
export default new Vuex.Store({
    state: {
        accessToken: null,
        refreshToken: null,
        userId: null,
        APIData: '',
    },

    mutations: {
        updateStorage (state, {access, refresh , userId: userId}) {
            state.accessToken = access
            state.refreshToken = refresh
            state.userId = userId
        },
        destroyToken (state) {
          state.accessToken = null
          state.refreshToken = null
          state.userId = null
        }
    },

    getters: {
        loggedIn (state) {
            return state.accessToken != null
        }
    },

    actions: {
        userLogout (context) {
            if (context.getters.loggedIn) {
                context.commit('destroyToken')
            }
        },
        userLogin (context, userCredentials) {
            return new Promise((resolve, reject) => {
                getAPI.post('/api-token/', {
                    username: userCredentials.username,
                    password: userCredentials.password
                })
                .then(response => {
                    context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh, userId: response.data.userId })
                    resolve()
                })
                .catch(err => {
                  reject(err)
                })
            })
        },
    }
})