import pymongo
from pymongo import collection
if __name__=="__main__":
    print("pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['shivam']
    collection=db['samplecollectionshivam']
    # one=collection.find_one({'name':'shivam'})
    # print(one)
    # all_docs=collection.find({'name':'shivam'})
    all_docs=collection.find({'name':'pk','marks':{'$gte':80}},{'name':1,'_id':0})
    # print(all_docs.count())
    print(collection.count_documents({'name':'pk','marks':{'$gte':80}}))
    for item in all_docs:
        print(item)

    
