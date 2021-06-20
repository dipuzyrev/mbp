module.exports = {
    pwa: {
      themeColor: "#ff5a5a",
      msTileColor: "#ff5a5a",
      appleMobileWebAppCapable: "yes",
      appleMobileWebAppStatusBarStyle: "black-translucent",
  
      manifestOptions: {
        name: "Мое давление",
        short_name: "Давление",
        start_url: ".",
        display: "standalone",
        theme_color: "#ff5a5a",
      },  
    },
    devServer: {
      proxy: {
        '^/api/': {
          target: 'http://localhost:8000',
          pathRewrite: { "^/api/": "/api/" },
          logLevel: "debug",
          changeOrigin: true
        }
      }
    }
  }