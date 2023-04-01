from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class Source(str, Enum):
    email = "email"
    file = "file"
    chat = "chat"


class DocumentMetadata(BaseModel):
    document_id: Optional[str] = None   
    price_from: Optional[Decimal] = None
    product_url: Optional[str] = None
    title: Optional[str] = None
    tag_line: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    country: Optional[str] = None

class DocumentChunkMetadata(DocumentMetadata):
    document_id: Optional[str] = None


class DocumentChunk(BaseModel):
    id: Optional[str] = None
    text: str
    metadata: DocumentChunkMetadata
    embedding: Optional[List[float]] = None


class DocumentChunkWithScore(DocumentChunk):
    score: float


class Document(BaseModel):
    id: Optional[str] = None
    text: str
    metadata: Optional[DocumentMetadata] = None


class DocumentWithChunks(Document):
    chunks: List[DocumentChunk]


class DocumentMetadataFilter(BaseModel):
    document_id: Optional[str] = None   
    price_from: Optional[Decimal] = None
    product_url: Optional[str] = None
    title: Optional[str] = None
    tag_line: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    country: Optional[str] = None


class Query(BaseModel):
    query: str
    filter: Optional[DocumentMetadataFilter] = None
    top_k: Optional[int] = 3


class QueryWithEmbedding(Query):
    embedding: List[float]


class QueryResult(BaseModel):
    query: str
    results: List[DocumentChunkWithScore]
