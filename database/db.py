from flask_pymongo import PyMongo

def init_db(app):
    mongo_uri = "mongodb://localhost:27017/citizenai"  # Hardcoded MongoDB URI
    print(f"✅ Loaded MONGO_URI: {mongo_uri}")  # Debug print
    app.config["MONGO_URI"] = mongo_uri
    mongo = PyMongo(app)
    return mongo
