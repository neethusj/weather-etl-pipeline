import requests
from mongo_connection import get_mongo_collection
from datetime import datetime

#------------------------------------------------------------------------
# Get reference to the 'live_weather' collection inside the 'Weather_data' 
# database in MongoDB
#-------------------------------------------------------------------------

collection,client=get_mongo_collection("Weather_data","live_weather")


#--------------------------------------------------------------------------
#Define API end point
#---------------------------------------------------------------------------

#Latitude and Longitude of Tvm city
required_latitude=8.5241
required_longitude=76.9366

#Construct the URL dynamically using latitude and longitude
url=f"https://api.open-meteo.com/v1/forecast?latitude={required_latitude}&longitude={required_longitude}&hourly=temperature_2m"

#----------------------------------------------------------------------------
#Fetch data from API
#----------------------------------------------------------------------------

response=requests.get(url)
if response.status_code==200:
    print("Success")
    data=response.json()

    #-----------------------
    #Extract Data
    #-----------------------

    result_latitude=data.get('latitude')
    result_longitude=data.get('longitude')
    result_timezone=data.get('timezone')
    result_hourly=data.get('hourly',{}) #{'time':[],'temperature_2m':[]}
    result_time=result_hourly.get('time',[])
    result_temp=result_hourly.get('temperature_2m',[])
    parsed_data=[]
    for time,temp in zip(result_time,result_temp):
        document={
            "latitude":result_latitude,
            "longitude":result_longitude,
            "timezone":result_timezone,
            "timestamp":datetime.strptime(time,"%Y-%m-%dT%H:%M"),
            "temperature":temp
        }
        parsed_data.append(document)

    #---------------------------------------------------------
    #Store Data in MongoDB
    #---------------------------------------------------------
    
    insert_result=collection.insert_many(parsed_data)
    print("Inserted",len(insert_result.inserted_ids),"records inserted into Mongo DB")
    
else:
    print("Error",response.status_code)
client.close()