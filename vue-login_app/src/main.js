import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './axios.js'
// import 'mdb-vue-ui-kit/css/mdb.min.css';
// import './index.js'

const app = createApp(App);
app.use(router);
app.mount('#app');
