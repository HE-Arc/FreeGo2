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
        updateStorage (state, {access, refresh , userId: userId}) {
            state.accessToken = access
            state.refreshToken = refresh
            state.userId = userId
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
                    context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh, userId: response.data.userId })
                    resolve()
                    getAPI.get('/notification/', {
                        params: {
                            user: this.state.userId,
                        }
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

        updateNotifications: function({commit}, notificationsAmount) {
            commit('updateNotificationsAmount', {notificationsAmount})
        },
    }
})