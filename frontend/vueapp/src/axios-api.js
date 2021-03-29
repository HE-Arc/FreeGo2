import axios from 'axios'

const getAPI = axios.create({
    //baseURL: process.env.VUE_APP_NOT_SECRET_CODE,
    baseURL: 'http://127.0.0.1:8000/backend',
    timeout: 1000,
})

export { getAPI }