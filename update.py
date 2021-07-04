import pymongo
from pymongo import collection
if __name__=="__main__":
    print("pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['shivam']
    collection=db['samplecollectionshivam']
    prev={"name":"shivam"}
    nextt={'$set':{"location":"california"}}
    # collection.update_one(prev,nextt)
    
    # collection.update_many(prev,nextt)
    up=collection.update_many(prev,nextt)
    print(up.modified_count)
    
