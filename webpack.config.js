const webpack = require('webpack');
const path = require('path');

module.exports = {
    mode: 'development',
    entry: [
        //'webpack-dev-server/client?http://localhost:8080', TODO
        './frontend/src/index.js'
    ],
    output: {
        path: path.resolve(__dirname, './static/js/'),
        filename: 'bundle.js',
        publicPath: 'http://localhost:8080/',
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react']
                    }
                }
            }
        ]
    },
    devServer: {
        static: {
            directory: path.join(__dirname, 'static'),
        },
        hot: false, // TODO
        port: 8080,
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
        //new webpack.HotModuleReplacementPlugin() TODO
    ]
};
