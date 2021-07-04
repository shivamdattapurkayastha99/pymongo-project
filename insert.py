import pymongo
from pymongo import collection
if __name__=="__main__":
    print("pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['shivam']
    collection=db['samplecollectionshivam']
    # dictionary={'name':'shivam','marks':100}
    # collection.insert_one(dictionary)
    # dictionary2={'name':'shivam3','marks':50}
    # collection.insert_one(dictionary2)
    insertThese=[
        {'_id':1,'name':'shivam','location':'Kolkata','marks':95},
        {'_id':2,'name':'pk','location':'Mumbai','marks':85},
    ]
    collection.insert_many(insertThese)