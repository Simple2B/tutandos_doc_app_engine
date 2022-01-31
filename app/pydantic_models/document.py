from typing import List
from pydantic import BaseModel


class Metadata(BaseModel):
    date: str
    client_name: str
    location: str


class SectionBase(BaseModel):
    number: str
    title: str
    score: float


class SectionData(SectionBase):
    scope: str


class SubsectionData(SectionBase):
    comments: str


class DataItem(BaseModel):
    metadata: Metadata
    sectionDataList: List[SectionData]
    subsectionDataList: List[SubsectionData]


class DocumentModel(BaseModel):
    dataItem: DataItem


class DocumentGeneratedResponse(BaseModel):
    success: bool
    document_uuid: str
