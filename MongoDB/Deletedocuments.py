import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydata"]
mycol = mydb["customers"]

# delete all documents where the address starts with the letter "P"

myquery = { "address": {"$regex": "^P"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")