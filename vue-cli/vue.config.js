module.exports = {
  publicPath: '',
  css: {
    loaderOptions: {
      scss: {
        additionalData: `@import "@/assets/sass/main.scss";` //@はsrcと同義
      }
    }
  },
  devServer: {
    proxy: (process.env.SABI_ENV)? 'http://python.sabi-service-group:3000': 'http://python:3000',
  }
}
