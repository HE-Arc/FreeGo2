import axios from 'axios'
import store from './store.js'

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000/backend',
    timeout: 5000,
})

getAPI.interceptors.response.use(response => {
  return response
}, async function (error) {
  const originalRequest = error.config
  if (error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true
    store.dispatch('userLoginRefresh')
    .then(() => {
      originalRequest.headers.Authorization = `Bearer ${JSON.parse(sessionStorage.getItem('token')).access}`
      return getAPI(originalRequest)
    })
    .catch(err => {
        console.log(err)
    })
  }
  return Promise.reject(error)
})

export { getAPI }