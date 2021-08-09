import  requests
from bs4 import BeautifulSoup
import json
from pymongo import MongoClient

from pprint import pprint

#connection="mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
#client=MongoClient(connection)
#print (client.list_database_names())
#db=client.Test
#cc=db.Test
#cc.find()

myclient = MongoClient("mongodb://localhost:27017/")
#print (myclient.list_database_names())
mydb = myclient["Test"]
mycol = mydb["TheCrawledData"]

#page = requests.get("https://api.rrpcanada.org/supplies")
#soup=BeautifulSoup(page.content,"lxml" )



res = requests.get("https://api.rrpcanada.org/supplies")
res.raise_for_status()
data = res.json()


for key in data['content']['content']:
    #print(key['minimumOrder'],key['productName'])
    mycol.insert_one({"Product_Name":key['productName'],"Total_Available":key['minimumOrder']})

        

