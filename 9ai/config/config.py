
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://yash12628:1234x@9aiapp.7kssw1z.mongodb.net/?retryWrites=true&w=majority&appName=9aiapp"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.Blogging 
blogs_collection = db["blogs"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)