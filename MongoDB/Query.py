import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydata"]
mycol = mydb["customers"]

# Find documents where the address field starts with the letter "P":
myquery = { "address": { "$regex": "^P" } }
mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

print("-------------------------------")

# Find documents where the address field starts with the letter "S" or higher:
myquery = { "address": { "$gt": "S" } }
mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

print("-------------------------------")
# Limit the result to only return 5 documents:

myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)