import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydata"]
mycol = mydb["customers"]

# Sort the result alphabetically by name
mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)

print("-------------------------------")

# Sort the result reverse alphabetically by name
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)