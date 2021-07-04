import pymongo
from pymongo import collection
if __name__=="__main__":
    print("pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    