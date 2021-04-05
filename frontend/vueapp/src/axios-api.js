import axios from 'axios'
import Cookies from 'js-cookie'

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000/backend',
    timeout: 5000,
    headers: {
      "X-CSRFTOKEN": Cookies.get('csrftoken')
    },
})

export { getAPI }