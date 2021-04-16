import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from './axios-api'

Vue.use(Vuex)
export default new Vuex.Store({
    strict: true,

    state: {
        accessToken: null,
        refreshToken: null,
        userId: null,
        APIData: '',
        notificationsAmount: null,
    },

    mutations: {
        updateStorage (state, {access, refresh , userId}) {
            state.accessToken = access
            state.refreshToken = refresh
            state.userId = userId
        },
        updateAccess (state, {access}) {
            state.accessToken = access
        },
        destroyToken (state) {
            state.accessToken = null
            state.refreshToken = null
            state.userId = null
        },
        updateNotificationsAmount(state, {notificationsAmount}) {
            // For some reason notificationsAmount is a Number on first call and an object later...
            if(notificationsAmount.notificationsAmount) {
                state.notificationsAmount = notificationsAmount.notificationsAmount
            }
            else {
                state.notificationsAmount = notificationsAmount
            }
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
                    sessionStorage.setItem('token', JSON.stringify(response.data))
                    context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh, userId: response.data.userId })
                    getAPI.get('/notification/', {
                        params: {
                            user: this.state.userId,
                        },
                        headers: {
                          'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('token')).access}`
                        },
                    })
                    .then(response => {
                        context.commit('updateNotificationsAmount', {notificationsAmount: response.data.length})
                        resolve()
                    })
                    .catch(err => {
                        reject(err)
                    })
                })
                .catch(err => {
                    reject(err)
                })
                
            })
        },

        userLoginRefresh (context) {
            return new Promise((resolve, reject) => {
                getAPI.post('/api-token-refresh/', {
                    refresh: this.state.refreshToken,
                })
                .then(response => {
                    let jsonToken = JSON.parse(sessionStorage.getItem('token'))
                    jsonToken.access = response.data.access
                    sessionStorage.setItem('token', JSON.stringify(jsonToken))
                    context.commit('updateAccess', { access: response.data.access })
                    resolve()
                })
                .catch(err => {
                    reject(err)
                })
            })
        },

        updateNotifications: function({commit}, notificationsAmount) {
            commit('updateNotificationsAmount', {notificationsAmount})
        },
    }
})