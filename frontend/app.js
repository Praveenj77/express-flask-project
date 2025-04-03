require("dotenv").config();
const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.set("view engine", "ejs");

const BACKEND_URL = process.env.BACKEND_URL || "http://localhost:5000";

app.get("/", (req, res) => {
    res.render("form");
});

app.post("/submit", async (req, res) => {
    try {
        const response = await axios.post(`${BACKEND_URL}/submit`, req.body);
        res.send(`Response from Flask: ${JSON.stringify(response.data)}`);
    } catch (error) {
        res.send("Error communicating with backend");
    }
});

app.listen(3000, () => {
    console.log("Frontend running on http://localhost:3000");
});
