// import { createApp } from 'vue'
// import App from './App.vue'
// import router from "./router";
//
// // createApp(App,
// //     router,
// //     ).mount('#app')
//
// createApp(App).use(router).mount('#app')
import Vue from 'vue'
import App from './App.vue'
import router from './router'
// import store from './store'

Vue.config.productionTip = false

new Vue({
  router,
  // store,
  render: h => h(App)
}).$mount('#app')