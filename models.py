from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class Node(BaseModel):
    id: int
    label: Optional[str] = None
    name: Optional[str] = None
    screen_name: Optional[str] = None
    sex: Optional[int] = None
    home_town: Optional[str] = None


class RelationshipType(str, Enum): # Валидируем тип связи
    FOLLOW = "Follow"
    SUBSCRIBE = "Subscribe"


class Relationship(BaseModel):
    id: Optional[int] = None  # Используется для идентификатора связи
    type: RelationshipType  # Тип связи
    end_node_id: int  # Конечный узел


class InsertRequest(BaseModel):
    node: Node
    relationships: List[Relationship]