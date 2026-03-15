require("dotenv").config()
const express = require("express")
const app = express() 
const mongoose = require("mongoose")

mongoose.connect(process.env.CONNECTIONSTRING)
    .then(() => {
        app.emit("Ready")
    })
    .catch(e => console.log(e))

const session = require("express-session")
const MongoStore = require("connect-mongo").default
const flash = require("connect-flash")
const routes = require("./routes")
const path = require("path")
const helmet = require("helmet")
const csrf = require("csurf")
const { global_middleware, check_csrf_error, csrf_middleware } = require("./src/middlewares/middleware.js")

app.use(helmet())

app.use(express.urlencoded({ extended: true }))
app.use(express.json())
app.use(express.static(path.resolve(__dirname, "public")))

const mongo_store = MongoStore.create({
  mongoUrl: process.env.CONNECTIONSTRING,
  collectionName: 'sessions',
});

const session_options = session({
    secret: "ABCDEFG",
    store: mongo_store,
    resave: false,
    saveUninitialized: false,
    cookie: {
        maxAge: 1000 * 60 * 60 * 24 * 7,
        httpOnly: true
    }
})

app.use(session_options)
app.use(flash())

app.set("views", path.resolve(__dirname, "src", "views"))
app.set("view engine", "ejs")

app.use(csrf())

app.use(global_middleware)
app.use(check_csrf_error)
app.use(csrf_middleware)
app.use(routes)

app.on("Ready", () => {
    app.listen(3000, () => {
        console.log("Server running on http://localhost:3000/")
    })
})