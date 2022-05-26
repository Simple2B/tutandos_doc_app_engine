from app.pydantic_models import FirebaseToken
from app.pydantic_models import ResponseMessage
from flask_jwt_extended import create_access_token
import datetime
from flask_openapi3.models import Tag
from app.views.v1.blueprint import BlueprintApi
import firebase_admin
from firebase_admin import auth

# Set up Bluerints
SECURITY = [{"jwt": []}]
TAG = Tag(name="Auth", description="Authentification via Firebase id token")
api_auth = BlueprintApi("/auth", __name__, abp_tags=[TAG], abp_security=SECURITY)


@api_auth.post("/login", responses={"200": ResponseMessage, "403": ResponseMessage})
def login_post(body: FirebaseToken):
    # Verify firebase account by id token
    try:
        decoded_token = auth.verify_id_token(body.id_token)
    except firebase_admin._auth_utils.InvalidIdTokenError:
        return ResponseMessage(success=True, description="Invalid token").dict(), 403

    uid = decoded_token["uid"]
    expires = datetime.timedelta(minutes=30)
    access_token = create_access_token(identity=str(uid), expires_delta=expires)
    headers = {"Authorization": f"Bearer {access_token}"}
    return ResponseMessage(success=True, description="Logged in").dict(), 200, headers
