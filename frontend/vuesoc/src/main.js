import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store'

let app = createApp(App).use(store);

app.use(router);

const localize = (key) => {
    const currentLocale = store.state.locale;
    let localeDict = require(`./locales/${currentLocale}.json`);
    return localeDict[key];
}

app.provide('l', localize);

app.mount('#app');
