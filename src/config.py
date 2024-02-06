import json
import os
from dotenv import load_dotenv

load_dotenv()

DatabaseJson = {
    "db": {
            "url": os.environ.get('URL_MONGODB_DEV'),
            "name": "tododb",
            "user" : "",
            "password" :""
    }
}

# config = json.load(DatabaseJson)
config = DatabaseJson
