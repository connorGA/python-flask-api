from flask import Flask, request, redirect, render_template
from bson.objectid import ObjectId
import json
from pymongo import MongoClient
import bson.json_util as json_util
# import datetime so we can have timestamps on things we add to the database.
from datetime import datetime
# import pprint so we can pretty print objects from the database.
import pprint
app = Flask(__name__, static_folder='static', static_url_path='/public')
# pymongo connects to the default host and port if you don't specify any
# parameters to the constructor when it's initialized. If you need to connect
# to a non-default MongoDB on your local machine then simply specify the host
# and port:
# host = 'localhost'
# port = 27017
# client = MongoClient(host, port)
# the default should set you up to use MongoClient('localhost', 27017)
client = MongoClient()
db = client.mongo_flask

db.drop_collection("redditpost")

# used to parse mongo data from bson to json so flask can send this data back to users
def parse_json(data):
    return json_util.dumps(data)

# creating a schema for our pymongo collection, not require wiht pymongo, but maybe a good idea
def create_reddit_post_collection(db):
    result = db.create_collection("redditpost", validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'required': ['userName', 'content', 'date', 'subreddit'],
            'properties': {
                'userName': {
                    'bsonType': 'string'
                },
                'content': {
                    'bsonType': 'string'
                },
                'subreddit': {
                    'bsonType': 'string'
                },
                'userid': {
                    'bsonType': 'string'
                },
                'date': {
                    'bsonType': 'date',
                },
                'location': {
                    'bsonType': 'string'
                }
            }
        }
    })
    print(result)

@app.route("/")
def hello():
    redirect = request.args.get('redirect')
    if not redirect:
        return "hello world!"
    else:
        return render_template(f'{redirect}.html')

@app.route("/render")
def get_render_template():
    return render_template('rendertemplate.html')

@app.route("/redirect")
def get_redirect():
     return redirect('/?redirect=redirect')

@app.route("/profile/<username>")
def profile(username):
  return "You're viewing {}'s profile.".format(username)

@app.route("/r/<string:subreddit>")
def reddit(subreddit):
    subreddits = db.redditpost.find({'subreddit': subreddit})
    pprint.pprint(subreddits)
    # keep note, there is a json.load and a json.loads function in our json module. json.loads changes a string to a usable python object(can be returned as json by flask)
    # the json.load function is used to deserialize a file into a json format. This would be useful when dealing with files, not useful when converting a string to json
    return json.loads(parse_json(subreddits))

# you can specify type inside of your routes, this is helpful for many reasons, but mostly for clarity and avoiding extra parsing
@app.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
  result = num1 * num2
  return str(result)

@app.route("/subreddit/<string:subreddit>/<string:user_id>", methods = ['POST', 'PUT'])
def create_subreddit(user_id, subreddit):
    data = request.form
    # url?local=USa
    location = request.args.get('locale')
    if request.method == 'POST':
        post = {
            'userName': data.get('userName'),
            'content': data.get('content'),
            'date': datetime.now(),
            'userid': user_id,
            'subreddit': subreddit,
            'location': location
        }
        post_id = db.redditpost.insert_one(post).inserted_id
        return str(post_id)
    if request.method == 'PUT':
        filter = {
            'subreddit': subreddit,
            'userid': user_id
        }
        newValues = { '$set': {
            'userName': data.get('userName'),
            'content': data.get('content'),
            'date': datetime.now(),
        }}
        db.redditpost.update_one(filter, newValues)
        subreddits = db.redditpost.find({'subreddit': subreddit})
        return json.loads(parse_json(subreddits))
        
# ///////////////////////////////////////////////////////////////////////
def create_blog_post_collection(db):
    result = db.create_collection("blogpost", validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'required': ['userName', 'content', 'date', 'title'],
            'properties': {
                'userName': {
                    'bsonType': 'string'
                },
                'content': {
                    'bsonType': 'string'
                },
                'title': {
                    'bsonType': 'string'
                },
                'userid': {
                    'bsonType': 'string'
                },
                'date': {
                    'bsonType': 'date',
                },
                'location': {
                    'bsonType': 'string'
                }
            }
        }
    })
    print(result)

@app.route("/blogpost/<string:title>")
def blog(title):
    titles = db.blogpost.find({'title': title})
    pprint.pprint(titles)
    return json.loads(parse_json(titles))


@app.route("/blog/<string:title>/<string:user_id>", methods = ['POST', 'PUT'])
def create_title(user_id, title):
    data = request.form
    # url?local=USa
    location = request.args.get('locale')
    if request.method == 'POST':
        post = {
            'userName': data.get('userName'),
            'content': data.get('content'),
            'date': datetime.now(),
            'userid': user_id,
            'title': title,
            'location': location
        }
        post_id = db.blogpost.insert_one(post).inserted_id
        return str(post_id)
    if request.method == 'PUT':
        filter = {
            'title': title,
            'userid': user_id
        }
        newValues = { '$set': {
            'userName': data.get('userName'),
            'content': data.get('content'),
            'date': datetime.now(),
        }}
        db.blogpost.update_one(filter, newValues)
        titles = db.blogpost.find({'title': title})
        return json.loads(parse_json(titles))

# ROMES ROUTES
@app.route('/cars', methods = ['POST', 'GET'])
def create_car():
    data = request.form
    if request.method == 'POST':
        car = {
            'make': data.get('make'),
            'model': data.get('model'),
            'date': datetime.now(),
            'color': data.get('color'),
            'mileage': data.get('mileage')
        }
        car_id = db.cars.insert_one(car).inserted_id
        print('yoooo -> ', car_id)
        new_car = db.cars.find_one({ '_id': car_id })
        return json_util.dumps(new_car)
    else:
        cars = db.cars.find()
        return json_util.dumps(cars)

@app.route('/cars/<string:car_id>', methods= ['PUT', 'GET', 'DELETE'])
def one_car(car_id):
    data = request.form
    print('this is a car', car_id)

    if request.method == 'PUT':
        '''update the car'''
        car = {
            'make': data.get('make'),
            'model': data.get('model'),
            'date': datetime.now(),
            'color': data.get('color'),
            'mileage': data.get('mileage')
        }
        db.cars.find_one_and_update({ '_id': ObjectId(car_id) }, { '$set': car })
        updated_car = db.cars.find_one({'_id': ObjectId(car_id)})
        return json_util.dumps(updated_car)

    elif request.method == 'DELETE':
        '''delete the car'''
        response = db.cars.find_one_and_delete({ '_id': ObjectId(car_id)})
        print('what is the response', response)
        return json_util.dumps(response)
    else:
        car = db.cars.find_one({ '_id': ObjectId(car_id) })
        # cars = db.cars.find()
        # print('this is a car', car_id)
        return json_util.dumps(car)









# when a file is ran as the entry point of a project, its '__name__' global property will be '__main__', if the module was imported, this will instead be the name of the module
# This conditional is to ensure that we do not run this server unintentionally if it wasn't the entry point for the project.
if __name__ == "__main__":
    app.run()
    create_reddit_post_collection(db)