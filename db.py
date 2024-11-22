import os
from dotenv import load_dotenv
from py2neo import Graph

# Загрузка переменных окружения
load_dotenv()


class Neo4jConnection:
    """
    Singleton для управления подключением к Neo4j.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Инициализация подключения
            bolt_url = os.getenv("NEO4J_BOLT_URL")
            user = os.getenv("NEO4J_USER")
            password = os.getenv("NEO4J_PASSWORD")
            cls._instance = Graph(bolt_url, auth=(user, password))
        return cls._instance
