const express = require("express")
const route = express.Router()

const home_controller = require("./src/controllers/home_controller")

route.get("/", home_controller.get_home)
route.post("/", home_controller.post_home)

module.exports = route