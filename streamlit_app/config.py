from decouple import config


API_URL = config("API_URL", "http://localhost:8000")

