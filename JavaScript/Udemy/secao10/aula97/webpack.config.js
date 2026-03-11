const path = require("path")

module.exports = {
    mode: "production",
    entry: path.resolve(__dirname, "frontend", "main.js"),

    output: {
        path: path.resolve(__dirname, "public", "assets", "js"),
        filename: "bundle.js"
    },
    module: {
        rules: [{
            exclude: /node_modules/,
            test: /\.js$/,
            use: {
                loader: "babel-loader",
                options: {
                    sourceType: "unambiguous",
                    presets: ["@babel/preset-env"]
                }
            }
        }, {
            test: /\.css$/,
            use: ["style-loader", "css-loader"]
        }]
    },
    devtool: "source-map"
}