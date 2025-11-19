from mongo_connection import get_mongo_collection
from mysql_connection import get_mysql_connection

#------------------------------------------------
# Connect to MySQL
#------------------------------------------------

conn=get_mysql_connection()
new_cursor=conn.cursor()

#--------------------------------------------------
# Create target table if it doesnot exists
# Create mysql database manually
#--------------------------------------------------

new_cursor.execute("""CREATE TABLE IF NOT EXISTS
                      live_weather (id int auto_increment primary key,
                                  latitude float,longitude float,
                                  timezone varchar(50),timestamp  datetime,
                                  temperature float)""")
conn.commit()

#------------------------------------------------------------------
# Connect to MongoDB
#------------------------------------------------------------------

# Get reference to 'live_weather' collection inside 'Weather_data' database
collection,client=get_mongo_collection('Weather_data','live_weather')

#----------------------------------------------------------------------
# Fetch data from MongoDB
#-----------------------------------------------------------------------

#Fetch all documents from MongoDB collection, excluding the internal '_id' field
#and store the values as a  list of tuples

query={}
projection={'_id':0}
values=[]
for doc in collection.find(query,projection):
    values.append((doc.get("latitude"),doc.get("longitude"),doc.get("timezone"),doc.get("timestamp"),doc.get("temperature")))


#-------------------------------------------------------------------------------
# Insert values into MySql database
#--------------------------------------------------------------------------------

sqlquery="""insert into live_weather(latitude,longitude,timezone,timestamp,temperature) 
            values(%s,%s,%s,%s,%s)"""
new_cursor.executemany(sqlquery,values)
conn.commit()
print(new_cursor.rowcount,"records inserted")
new_cursor.close()
conn.close()
client.close()

