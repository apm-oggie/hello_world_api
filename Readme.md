# Hello World API with Flask

This project demonstrates how to create a simple "Hello World" API using Flask and build a webpage to interact with it. Follow the steps below to set up the project from scratch.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Project Setup](#project-setup)
- [Creating the API](#creating-the-api)
- [Running the API](#running-the-api)
- [Creating the Webpage](#creating-the-webpage)
- [Testing the Webpage](#testing-the-webpage)
- [Deploying to Heroku (Optional)](#deploying-to-heroku-optional)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

1. **Python**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Visual Studio Code**: Download and install VSCode from [code.visualstudio.com](https://code.visualstudio.com/).
3. **Heroku CLI** (optional for deployment): Follow instructions at [Heroku CLI Installation](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

## Project Setup

1. **Create a Project Directory**:
   Open a terminal and create a new directory for your project:
   
   mkdir hello_world_api
   cd hello_world_api

2. **Create a Virtual Environment (optional): If dont want any issue related to python installation , add the path in environment   variables.

     python -m venv venv

Activate the virtual environment:
On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install Flask:
Install Flask using pip:
pip install Flask flask-cors

Creating the API
Create the API File:
In your project directory, create a file named app.py.
Write the API Code:
Open app.py in VSCode and write the code which is specifically present in app.py file .


Creating the Webpage
Create an HTML File:
In your project directory, create a file named index.html.
Write the HTML Code:
Open index.html in VSCode and write the code already present in .html file .


#####  Deploying to Heroku (Optional)



If you want to deploy your application to Heroku, follow these additional steps:
Set Up Heroku CLI:
Ensure you have installed Heroku CLI as described in the prerequisites.
Prepare Your Application for Deployment:
1. Create a file named requirements.txt in your project directory with the following content:
Flask==2.0.1
gunicorn==20.1.0
flask-cors==3.0.10  # Include flask-cors if used in app.py

2. Create a file named Procfile (with no file extension) containing:
web: gunicorn app:app

3. Deploy Your Application:
Initialize a Git repository in your project directory:
bash
git init
git add .
git commit -m "Initial commit"

4. Create a new Heroku application and deploy it:
bash
heroku create
git push heroku master

Access Your Application:
Once deployed, you can access your application using the URL provided by Heroku.


