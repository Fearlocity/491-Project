# **Plant Care**
This project can assist users in identifying plants, including any possible illness that may be affecting the plants, in their backyards and to help remind them when to water their plants. It can also be able to aid users in determining what plants are best for them according to their preferences.

## Requirements
[TensorFlow](https://www.tensorflow.org/install/pip#linux)
[Node.js](https://nodejs.org/en)
[MongoDB Cloud Database](https://www.mongodb.com/)

## Installation and Running
### Prerequisites:
	Node.js: Make sure node.js is installed on your machine. 
	Git: Make sure git is installed on your machine. 
	Follow TensorFlow installation guide to install all related dependencies
### Steps:
- Clone the Repository: git clone https://github.com/Fearlocity/491-Project
- Navigate to Project Directory: cd 491-Project
- Install Dependencies: npm install dotenv express express-session mongoose nodemon bcrypt
- Set Environmental Variables:
- Create a ‘.env’ file in the projects root directory
- Add the following to the ‘.env’ file: MONGO_URI = 'mongodb+srv://tbryant3614:fear@plantcar.ztl8ecg.mongodb.net/user?retryWrites=true&w=majority'
- This is the connection link for the database. Please do not share.
- Run the Application: npm run dev
- Access the Application: Open a browser and go to ‘http://localhost:3000’ to access the website

## Authors
* Kelton Benson
* Nicholas Jones
* Timothy Bryant
