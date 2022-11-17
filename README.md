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

# Breakout room activity

Go into breakout rooms in groups of 2-3 and try to create a new post endpoint that will add records to a new collection. Once the record has been added, have the API endpoint return the ID of the newly created record. 

## requirements

1. You should create a new api endpoint that accepts POST http verbage requests
2. This endpoint should accept data passed to the API in the reuqest body and format that data into a new object that can be used to create a new record inside of a new collection
3. (optional): Feel free to create a schema function like we did for redditposts in our example, this is not required, but encouraged.
4. use pymongo to insert your new record into a new collection.
5. When the record is created successfully, return the String version of the ObjectId of our new record in the response of your newly created post endpoint. 
6. Use postman to test your endpoint and once you'r confirmed that it is working, export your updated postman collection to a json file and add it to the postman folder in this project. 

# library documentation

[Flask](https://flask.palletsprojects.com/en/2.2.x/installation/#python-version)
[Pymongo](https://pymongo.readthedocs.io/en/stable/).