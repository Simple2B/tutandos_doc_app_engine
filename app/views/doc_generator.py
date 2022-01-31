from app.views.blueprint import BlueprintApi
from app.logger import logger
from flask_openapi3.models import Tag
from flask_jwt_extended import jwt_required
from app.pydantic_models import DocumentModel, DocumentGeneratedResponse
from app.services import doc_generator


# Set up Bluerints
SECURITY = [{"jwt": []}]
TAG = Tag(name="DocGen", description="Create document")
api_docgen = BlueprintApi("/", __name__, abp_tags=[TAG], abp_security=SECURITY)


@api_docgen.post('/document', responses={"200": DocumentGeneratedResponse})
@logger.catch
@jwt_required()
def generate_document(body: DocumentModel):
    uuid = doc_generator.generate_doc(body.dict())
    return DocumentGeneratedResponse(success=True, document_uuid=uuid).dict(), 200
