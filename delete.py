import pymongo
from pymongo import collection
if __name__=="__main__":
    print("pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['shivam']
    collection=db['samplecollectionshivam']
    rec={"name":"shivam"}
    
    # collection.delete_one(rec)
    
    up=collection.delete_many(rec)
    print(up.deleted_count)
    
    
