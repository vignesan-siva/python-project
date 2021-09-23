#ctreate mongodb collection
"""import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
db=conn["math"]
c=db["mark"]
hello=db.list_collection_names()
if "student" in hello:
    print("true")
else:
    print("false")"""
#check mongo db database
"""import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
db=conn["math"]
c=db["student"]
hello=conn.list_database_names()
if "math" in hello:
    print("true")
else:
    print("false")"""
#insert one data
import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
db=conn["math"]
c=db["student"]
data={"name":"siva","id":"123"}
x=c.insert_one(data)
print(x)
#insert many
"""import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
db=conn["math"]
c=db["student"]
data=[{"name":"siva","id":"123",
"email":["saravanan","alamelu"]}]
x=c.insert_many(data)
print(x)"""
#find one data
"""import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
db=conn["math"]
c=db["student"]
for x in c.find({'name':'vignesan'}):
    print(x)"""

#find many all data
"""import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
db=conn["math"]
c=db["student"]
for x in c.find():
    print(x)"""
#update one
"""import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
db=conn["math"]
c=db["student"]
data={'name':'vignesan'}
new={'$set':{'name':'surya'}}#just more data and new values added to example 'df' variable to print
df=c.update_one(data,new)
print(df)"""
#delete one data
"""import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
db=conn["math"]
c=db["student"]
data={'name':'vignesan'}
df=c.delete_one(data)#same as delete many::""df=c.delete_many({})
print(df)"""
#delete all
"""import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
db=conn["math"]
c=db["student"]
x=c.drop()"""
