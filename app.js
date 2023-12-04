const http = require('http');
const fs = require('fs');
const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const User = require("./schemas/user");
const bcrypt = require('bcrypt');

require('dotenv').config()
const uri = process.env.MONGO_URI;
const app = express();
app.use(express.static(path.join(__dirname, 'Plant Care')));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


// Connect to MongoDB using Mongoose
mongoose
  .connect(uri)
  .then(() => {
    console.log("Connected to MongoDB");
  })
  .catch((error) => {
    console.error("Error connecting to MongoDB:", error);
  });

app.post("/register", async (req, res) => {
  const { username, password } = req.body;

  try {
    const existingUser = await User.findOne({ username });
    if (existingUser) {
      return res.redirect('/register?registerError=Username already in use.');
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    const newUser = new User({ username, password: hashedPassword });
    await newUser.save();

    console.log("Registration successful");
    res.status(201).sendFile(path.join(__dirname, '/Plant Care/login.html'))
  } catch (error) {
    console.error("Registration error:", error);
    res.redirect('/register?registerError=An error occurred during registration.');

  }
});

var user;
app.post("/login", async (req, res) => {
  const { username, password } = req.body;
  savedUserName = username

  try {
    user = await User.findOne({ username });

    if (!user) {
      return res.redirect('/login?loginError=Invalid username or password.');
    }

    const isPasswordValid = await bcrypt.compare(password, user.password);

    if (!isPasswordValid) {
      return res.redirect('/login?loginError=Invalid username or password.');
    }
    console.log("Login successful");
    res.status(201).sendFile(path.join(__dirname, '/Plant Care/index.html'))
  } catch (error) {
    console.error("Login error:", error);
    res.redirect('/login?loginError=An error occurred during login.');

  }
});

app.get('/register', (req, res) => {
  res.sendFile(path.join(__dirname, '/Plant Care/login.html'));
});

app.get('/login', (req, res) => {
  res.sendFile(path.join(__dirname, '/Plant Care/login.html'));
});

const server = http.createServer(app);

const port = process.env.PORT || 3000;

server.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});