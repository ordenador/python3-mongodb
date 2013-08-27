## Hello World Python3 with mongodb from: http://paulcolfer.ie/development/python/python-3-with-mongodb-2/
from pymongo import Connection
connection=Connection()
database=connection['strapingdb']
mycollection=database.entries

print("-------------------------Insert:")
post1={"title":"My first post","details":"This is my first entries on PyMongo"}
mycollection.insert(post1)
post2={"title":"My second post","date":"05/11/2012","author":"Paul"}
mycollection.insert(post2)


print(mycollection.find_one({"title":"My second post"}))

print("-------------------------all documents - 1:")
for entry in mycollection.find():
	print(entry)

print("-------------------------all documents - 2:")
for entry in mycollection.find({"title":"My first post"}):
	print(entry)
