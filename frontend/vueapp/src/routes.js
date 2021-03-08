import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home'
import Options from './views/Options'
import Fridge from './views/Fridge'
import Favorites from './views/Favorites'
import Login from './views/Login'
import Logout from './views/Logout'
import ContactUs from './views/ContactUs'
import Donations from './views/Donations'
import ManageFridge from './views/ManageFridge'
import Notifications from './views/Notifications'

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
            path: '/fridge/:fridgeId?',
            name: 'fridge',
            component: Fridge,
        },
        {
            path: '/favorites',
            name: 'favorites',
            component: Favorites,
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
        {
            path: '/notifications',
            name: 'notifications',
            component: Notifications,
        },
    ]
})