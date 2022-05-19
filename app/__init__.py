import os

# import requests
from supabase import create_client
from flask_jwt_extended import JWTManager
from flask_openapi3 import OpenAPI
from flask_openapi3.models import Info
from flask_openapi3.models.security import HTTPBearer

# from app.services import doc_generator
# import firebase_admin
from firebase_admin import auth


def create_app(environment="development"):
    from config import config

    # Instantiate app.
    info = Info(title="Skelet API", version="1.0.0")
    jwt = HTTPBearer(bearerFormat="JWT")
    securitySchemes = {"jwt": jwt}
    app = OpenAPI(__name__, security_schemes=securitySchemes, info=info)

    # Set app config.
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    config[env].configure(app)
    app.config["VALIDATE_RESPONSE"] = True
    # doc_generator.configure(config[env])

    from app.views import api_docgen, api_auth

    app.register_api(api_docgen)
    app.register_api(api_auth)

    jwt = JWTManager(app)

    # cred = firebase_admin.credentials.Certificate("firebase-admin-cred.cred.json")
    # firebase_admin.initialize_app(cred)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        user = auth.get_user(identity)
        return user

    return app


SUPABASE_URL = "https://utitytmrxlwyizpxegtv.supabase.co/rest/v1/testing_goods?select=*"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV0aXR5dG1yeGx3eWl6cHhlZ3R2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NTI4ODA5NDMsImV4cCI6MTk2ODQ1Njk0M30.40GTqnuw7QN9RxOyFpzl6yvNQ66brTUZPwg-Z42HcuY"
SUPABASE_BEARER_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV0aXR5dG1yeGx3eWl6cHhlZ3R2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NTI4ODA5NDMsImV4cCI6MTk2ODQ1Njk0M30.40GTqnuw7QN9RxOyFpzl6yvNQ66brTUZPwg-Z42HcuY"
SUPABASE_HEADERS = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": SUPABASE_BEARER_TOKEN,
}

# response = requests.get(f"{SUPABASE_URL}", headers=SUPABASE_HEADERS)
# print(response.text)

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)
query = supabase.table("testing_goods").select("*").execute()

for item in query.data:
    print(item)
