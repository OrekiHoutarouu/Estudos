const express = require("express")
const route = express.Router()

const home_controller = require("./src/controllers/home_controller")
const contato_controller = require("./src/controllers/contato_controller")

route.get("/", home_controller.get_home)
route.post("/", home_controller.post_home)

route.get("/contato", contato_controller.get_contato)

module.exports = route