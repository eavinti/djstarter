const webpack = require('webpack');
const path = require('path');

module.exports = {
    mode: 'development', // Establece el modo de desarrollo por defecto
    entry: [
        'webpack-dev-server/client?http://localhost:8080',  // Activar el hot reloading
        './frontend/src/index.js' // El punto de entrada de tu aplicación
    ],
    output: {
        path: path.resolve(__dirname, './static/js/'), // Donde se guardarán los archivos bundle
        filename: 'bundle.js',
        publicPath: 'http://localhost:8080/',
    },
    module: {
        rules: [
            {
                test: /\.js$/, // Para todos los archivos .js
                exclude: /node_modules/, // Excepto la carpeta node_modules
                use: {
                    loader: 'babel-loader', // Usa babel-loader
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react'] // Para transpilar ES6+ y React
                    }
                }
            }
        ]
    },
    devServer: {
        static: {
            directory: path.join(__dirname, 'static'), // Suponiendo que "static" es tu carpeta pública
        },
        hot: true,
        port: 8080, // Definir explícitamente el puerto, solo por claridad
        proxy: {
            '/static/js/': {
                target: 'http://localhost:8000',
                secure: false
            }
        },
        headers: {
            'Access-Control-Allow-Origin': '*',
        },
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin()
    ]
};
