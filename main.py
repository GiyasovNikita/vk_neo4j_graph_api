from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from queries import Neo4jQueries
from models import InsertRequest
import os
from dotenv import load_dotenv

app = FastAPI(
    title="Neo4j Graph API",
    description="API для работы с графовой базой данных Neo4j",
    version="1.0.0"
)

# Загрузка переменных окружения
load_dotenv()

# Настройка авторизации
auth_scheme = HTTPBearer()


def validate_token(credentials: HTTPAuthorizationCredentials = Security(auth_scheme)):
    token = credentials.credentials
    if token != os.getenv("AUTH_TOKEN"):
        raise HTTPException(status_code=401, detail="Invalid or missing token")


@app.get("/nodes", summary="Получение всех узлов", description="Возвращает список всех узлов с атрибутами id и label.")
def get_nodes():
    return Neo4jQueries.get_all_nodes()


@app.get("/node/{node_id}", summary="Получение узла и связей", description="Возвращает узел и все его связи.")
def get_node(node_id: int):
    return Neo4jQueries.get_node_and_relationships(node_id)


@app.post("/insert", summary="Добавление узла и связей", description="Добавляет узел и его связи в базу данных.")
def insert_graph(insert_request: InsertRequest, credentials: HTTPAuthorizationCredentials = Security(auth_scheme)):
    validate_token(credentials)
    Neo4jQueries.insert_node_and_relationships(insert_request.node, insert_request.relationships)
    return {"status": "Node and relationships added"}


@app.delete("/node/{node_id}", summary="Удаление узла и связей", description="Удаляет узел и его связи из базы данных.")
def delete_node(node_id: int, credentials: HTTPAuthorizationCredentials = Security(auth_scheme)):
    validate_token(credentials)
    Neo4jQueries.delete_node_and_relationships(node_id)
    return {"status": f"Node {node_id} and its relationships deleted"}
