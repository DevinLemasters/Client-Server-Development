from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.json_util import loads
import pandas as pd

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, userValue, passValue):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        username = userValue
        password = passValue
        self.client = MongoClient('mongodb://%s:%s@localhost:30797/AAC' % (username, password))
        self.database = self.client['AAC']

# Method for implementing Create in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # Inserts the data into the database, data should be dictionary.
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, data):
        if self.database.animals.find(data) is not None: 
            cur = self.database.animals.find(data) # Finds the data in the database, data should be dictionary.
            return cur
        else:
            raise Exception("Failed to find document!")
            return False
            
# Method for implementing Update in CRUD
    def update(self, oldData, newData):
        if self.database.animals.find(oldData):
            # Updates the old data with the new data, both data arguments should be dictionary.
            self.database.animals.update(oldData, {"$set": newData}) 
            # dumps turns an object into a JSON string.
            return dumps(self.database.animals.find(newData))
        else:
            raise Exception("Error, could not find data to update!")
            return False

# Method for implementing Delete in CRUD
    def delete(self, data):
        if self.database.animals.find(data):
            # Deletes the found data from the database, data should be dictionary.
            self.database.animals.delete_one(data)
            # dumps turns an object into a JSON string.
            return dumps(self.database.animals.find(data))
        else:
            raise Exception("Error, could not find data to delete!")
            return False
            
            