
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-icons/font/bootstrap-icons.css";
import 'font-awesome/scss/font-awesome.scss';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import 'lossless-json';

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.mount('#app')
