const mongoose = require("mongoose")

const home_schema = new mongoose.Schema({
    titulo: { type: String, required: true},
    descricao: String
})

const home_model = mongoose.model("Home", home_schema)

class Home {

}

module.exports = Home