import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000/backend',
    timeout: 5000,/* 
    headers: {
      "Authorization": "Bearer " + token
    }, */
})

export { getAPI }