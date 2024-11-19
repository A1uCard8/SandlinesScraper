client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["scraped_data_db"]  # Database name
collection = db["web_data"]  # Collection name
