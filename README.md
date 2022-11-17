# Setup

To run this project you must first install pip dependencies.

you must then turn on your local mongodb instance, as we will use that as our database for our project.

lastly, import the postman environment and collection json files into your local postman application, this will make testing our API much easier. 

## PIP setup

This project has a requirements.txt file, this is in many ways creating parity with out node.js package.json file, but it's not quite as easy to use as npm's package.json. 

to create a requirements.txt file, simply run the following

```
touch requirements.txt
```

If you look inside of the 'requirements.txt' file you'll see all packages used to create this demo project. 

You can install these packages using the following command

'''
pip install -r requirements.txt
'''

you can have pip update the requirements.txt file for you using the following command

'''
pip freeze > requirements.txt
'''

# What's inside of this project

This project shows how you can create API routes using python and Flask, this project also shows you how you can interact with mongodb using pymongo. 

Inside of this project we showcase how to search, create and update mongo documents using pymongo and Flask. 

We also show how you can connect to mongodb using pymongo and how you can define simple schema for mongodb, however pymongo doesn't require or really even encourage users to use schemas. 

We also show how you can set URL params and URL query params using Flask, we also show how you can define types to URL and query params. We also show how you can fetch data from a request body and how to create a GET, POST and PUT route using Flask. 

We showcase how you can setup a static file repository as we have done in node's express framework. 

We also showcase how you can use UI templates using the Flask render-template functionality and how we can conduct server side redirect using Flask. 

# Debugging

This project has a vscode launch.json pre-configured for debugging your python application locally.