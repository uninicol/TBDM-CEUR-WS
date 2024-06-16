from pymongo import MongoClient

class Database:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.papers_collection = self.db["papers"]
        self.volumes_collection = self.db["volumes"]

    def save_volume(self, volume_dict):
        print("Saving volume " + volume_dict["volnr"] + " to database")
        return self.volumes_collection.insert_one(volume_dict).inserted_id

    def save_paper(self, paper_dict):
        print("Saving paper " + paper_dict["title"] + " to database")
        self.papers_collection.insert_one(paper_dict)

    def volume_exists(self, volnr):
        return self.volumes_collection.find_one({"volnr": volnr}) is not None

    def get_volume_id(self, volnr):
        volume = self.volumes_collection.find_one({"volnr": volnr})
        return volume["_id"] if volume else None
