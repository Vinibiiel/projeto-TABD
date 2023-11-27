from pymongo import MongoClient


# EXEMPLO DE URL LOCAL
MONGO_URL = "mongodb://localhost:27017/" # INSERIR SUA URL MONGO AQUI

class Connection:
    def __init__(self):
        self.__client__ = None

    def connect_to_mongo(self):
        self.__client__ = MongoClient(MONGO_URL)
        db = self.__client__['TABD']
        return db

    def close_connection(self):
        self.__client__.close()
            
