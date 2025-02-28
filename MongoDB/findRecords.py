import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydata"]
mycol = mydb["customers"]

# returns only the first document in the customers collection
x = mycol.find_one()
print(x)

print("-------------------------------")

# returns all fields except _id (use 0 for exclusion)
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

print("-------------------------------")

# returns all fields except address (use 0 for exclusion)
for x in mycol.find({}, { "address": 0 }):
  print(x)