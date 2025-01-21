import pymongo
import json

mongodb_uri = "mongodb://localhost:27017/"
database_name = "mydatabase"
collection_name = "mycollection"


def insert_json_to_mongodb(
    json_file_path, db_name, collection_name, mongo_uri=mongodb_uri
):
    """
    Inserts data from a JSON file into a MongoDB collection.

    Args:
      json_file_path (str): The file path to the JSON file containing the data to be inserted.
      db_name (str): The name of the MongoDB database.
      collection_name (str): The name of the collection within the MongoDB database.
      mongo_uri (str): The MongoDB URI for connecting to the database. Defaults to the value of `mongodb_uri`.

    Raises:
      FileNotFoundError: If the JSON file does not exist.
      json.JSONDecodeError: If the JSON file contains invalid JSON.
      pymongo.errors.PyMongoError: If an error occurs while inserting data into MongoDB.

    Example:
      insert_json_to_mongodb('/path/to/file.json', 'mydatabase', 'mycollection', 'mongodb://localhost:27017/')
    """
    # Connect to MongoDB
    client = pymongo.MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Read JSON file
    with open(json_file_path, "r") as file:
        data = json.load(file)

    # Insert data into MongoDB collection
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

    print(f"Data inserted into {db_name}.{collection_name} successfully.")


# Example usage
if __name__ == "__main__":
    insert_json_to_mongodb("example.json", database_name, collection_name, mongodb_uri)
