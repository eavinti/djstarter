const path = require('path');

module.exports = {
    entry: './frontend/src/index.js', // El punto de entrada de tu aplicación
    output: {
        path: path.resolve(__dirname, './static/js/'), // Donde se guardarán los archivos bundle
        filename: 'bundle.js',
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
    }
};
