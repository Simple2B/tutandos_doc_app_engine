from uuid import UUID
from pydantic import BaseModel


# TODO remove in future
# class Metadata(BaseModel):
#     date: str
#     client_name: str
#     location: str


# class SectionBase(BaseModel):
#     number: str
#     title: str
#     score: float


# class SectionData(SectionBase):
#     scope: str


# class SubsectionData(SectionBase):
#     comments: str

# class DataItem(BaseModel):
#     metadata: Metadata
#     sectionDataList: List[SectionData]
#     subsectionDataList: List[SubsectionData]


class DocumentModel(BaseModel):
    audit_id: UUID


class DocumentGeneratedResponse(BaseModel):
    success: bool
    msg: str
    # data: list
