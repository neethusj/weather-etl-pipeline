from mongo_connection import get_mongo_collection

#---------------------------------------------------------------
# Connect to MongoDB
#----------------------------------------------------------------

collection,client=get_mongo_collection('Weather_data','live_weather')

#Check the count of documents in the collection
count=collection.count_documents({})
print(f"Total documents in collection:{count}")

if count==0:
    print("No documets found.....")
else:
    query={}
    projection={'_id':0}
    #------------------------------------------------------------------
    # Fetch all documents excluding the '_id' field and print it
    #------------------------------------------------------------------

    for doc in collection.find(query,projection):
        print(doc)
        
client.close()
   
