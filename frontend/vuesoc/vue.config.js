const { defineConfig } = require('@vue/cli-service');
const path = require('path');

module.exports = {
    configureWebpack: {
        resolve: {
            symlinks: false,
            extensions: ['.js', '.vue', '.json'],
            alias: {
              '@': path.resolve(__dirname, './src'),
              vue: path.resolve(`./node_modules/vue`)
            }
          }
    }
}