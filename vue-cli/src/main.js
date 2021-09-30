import Vue from 'vue'
import App from './App.vue'

//ここ以外にエントリーポイントを作りたい場合→マルチページモード

Vue.config.productionTip = false //注釈を出すだけ

new Vue({
  render: h => h(App), //render関数とは、htmlを関数で書く仕組み
}).$mount('#app')
