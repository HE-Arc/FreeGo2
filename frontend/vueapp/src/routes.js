import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home'
import Options from './views/Options'
import Fridge from './views/Fridge'
import Login from './views/Login'
import Logout from './views/Logout'
import ContactUs from './views/ContactUs'
import Donations from './views/Donations'
import ManageFridge from './views/ManageFridge'

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
        {
            path: '/fridge',
            name: 'fridge',
            component: Fridge,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/login',
            name: 'login',
            component: Login,
        },
        {
            path: '/logout',
            name: 'logout',
            component: Logout,
        },
        {
            path: '/contact',
            name: 'contactUs',
            component: ContactUs,
        },
        {
            path: '/donations',
            name: 'donations',
            component: Donations,
        },
        {
            path: '/manageFridge',
            name: 'manageFridge',
            component: ManageFridge,
        },
    ]
})