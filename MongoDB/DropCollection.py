import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["abc"]

# drop the collection "abc" in the database "abc"
mycol = mydb["abc"]

mycol.drop()