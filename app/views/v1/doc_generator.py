from app.views.v1.blueprint import BlueprintApi
from flask_openapi3.models import Tag
# from flask_jwt_extended import jwt_required
from app.pydantic_models import DocumentModel, DocumentGeneratedResponse
from app.services import service_document


# Set up Bluerints
# SECURITY = [{"jwt": []}]
TAG = Tag(name="DocGen", description="Create document")
# api_docgen = BlueprintApi("Document", __name__, abp_tags=[TAG], abp_security=SECURITY, url_prefix="/api/v1")
api_docgen = BlueprintApi("Document", __name__, abp_tags=[TAG], url_prefix="/api/v1")


@api_docgen.post("/document", responses={"200": DocumentGeneratedResponse})
def generate_document(body: DocumentModel):
    if not service_document.is_audit_exist(body.audit_id):
        return DocumentGeneratedResponse(success=False, msg=f"No audit with id: {body.audit_id}").dict(), 200

    answers = service_document.get_answers(body.audit_id)

    return DocumentGeneratedResponse(
        success=True,
        msg=f"Document generate started. Answers count: {len(answers)}"
    ).dict(), 200
