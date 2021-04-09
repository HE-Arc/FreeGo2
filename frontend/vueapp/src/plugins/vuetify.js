import '@mdi/font/css/materialdesignicons.css'
import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify);

export default new Vuetify({
    icons: {
        iconfont: 'mdi',
    },
    theme: {
        themes: {
            light: {
                primary: '#3bafc8',
                secondary: '#8c2977',
                accent: '#f07f30',
                //error: '#FF5252',
                info: '#5dcae4',
                success: '#6eaa19',
                //warning: '#FFC107',
            },
        },
    },
});
