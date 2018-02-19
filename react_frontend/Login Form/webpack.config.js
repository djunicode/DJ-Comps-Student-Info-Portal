var webpack = require('webpack');
var path = require('path');
var libraryName = 'Final_bundle';
var outputFile = libraryName + '.js';

var config = {
  entry: __dirname + '/src/index.js',
  output: {
    path: __dirname + '/build/',
    filename: outputFile,
    library: libraryName,
    libraryTarget: 'umd',
    umdNamedDefine: true
  },
  
  module: {
    loaders: [
      {
        test: /(\.jsx|\.js)$/,
        loader: 'babel-loader',
        exclude: /(node_modules|bower_components)/,
        
      },
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      }
    ]
  }
};


module.exports = config;
