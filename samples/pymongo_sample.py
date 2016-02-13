__author__ = 'izeye'

from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId
from pymongo import ASCENDING, DESCENDING

client = MongoClient()
# client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017')

db = client.test_database
# db = client['test-database']

collection = db.test_collection
collection = db['test_collection']

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert(post)
print post_id

print db.collection_names()

print posts.find_one()
print posts.find_one({"author": "Mike"})
print posts.find_one({"author": "Eliot"})
print posts.find_one({"_id": post_id})

post_id_as_str = str(post_id)
print posts.find_one({"_id": post_id_as_str})

print posts.find_one({"_id": ObjectId(post_id_as_str)})

new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]
print posts.insert(new_posts)

for post in posts.find():
    print post

for post in posts.find({"author": "Mike"}):
    print post

print posts.count()
print posts.find({"author": "Mike"}).count()

d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    print post

print posts.find({"date": {"$lt": d}}).sort("author").explain()["cursor"]
print posts.find({"date": {"$lt": d}}).sort("author").explain()["nscanned"]

print posts.create_index([("date", DESCENDING), ("author", ASCENDING)])

print posts.find({"date": {"$lt": d}}).sort("author").explain()["cursor"]
print posts.find({"date": {"$lt": d}}).sort("author").explain()["nscanned"]
