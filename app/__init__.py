import os
from flask_jwt_extended import JWTManager
from flask_openapi3 import OpenAPI
from flask_openapi3.models import Info
from flask_openapi3.models.security import HTTPBearer
from firebase_admin import auth
from app.services import db


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
    db.init_app(app)
    # doc_generator.configure(config[env])

    from app.views import api_docgen

    app.register_api(api_docgen)

    jwt = JWTManager(app)

    # cred = firebase_admin.credentials.Certificate("firebase-admin-cred.cred.json")
    # firebase_admin.initialize_app(cred)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        user = auth.get_user(identity)
        return user

    return app
