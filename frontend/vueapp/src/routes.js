import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home'
import Options from './views/Options'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home,
        },
        {
            path: '/options',
            name: 'options',
            component: Options,
        },
    ]
})