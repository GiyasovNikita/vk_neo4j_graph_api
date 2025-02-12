# VK Neo4j Graph API
VK Neo4j Graph API — это API для работы с графовой базой данных Neo4j, предназначенное для управления графом данных, таких как пользователи, фолловеры и подписки. API позволяет запрашивать данные из Neo4j, добавлять новые узлы и связи, а также удалять их.

## Функционал
- **Чтение данных из Neo4j:**
  - Получение всех узлов с их метками и ID.
  - Получение узла, всех его связей и связанных узлов.
- **Добавление данных:**
  - Создание новых узлов и связей в графе.
- **Удаление данных:**
  - Удаление узлов и связанных с ними связей.
## Установка и запуск
### Требования
- `Python`: версия 3.7 или выше
- `Neo4j`: версия 4.0 или выше
### Шаги установки
1. **Клонируйте репозиторий:**

```bash
git clone https://github.com/GiyasovNikita/vk_neo4j_graph_api.git
cd vk_neo4j_graph_api
```
2. **Создайте виртуальное окружение:**

```bash
python -m venv .venv
.venv\Scripts\activate
```
3. **Установите зависимости:**

```bash
pip install -r requirements.txt
```
4. **Настройте переменные окружения: Создайте файл `.env` в корневой директории и добавьте следующие переменные:**

```makefile
NEO4J_BOLT_URL=bolt://localhost:7687
NEO4J_USER=ваш_пользователь_neo4j
NEO4J_PASSWORD=ваш_пароль_neo4j
AUTH_TOKEN=ваш_токен_авторизации
```
5. **Запустите сервер:**

```bash
uvicorn main:app --reload
```
Сервис будет доступен по адресу: `http://127.0.0.1:8000`.

## Эндпоинты API
1. **Получение всех узлов**
- **URL:** `/nodes`
- **Метод:** `GET`
- **Описание:** Возвращает список всех узлов с их ID и метками.
- **Пример ответа:**
```json
[
    {"id": 1, "label": "User"},
    {"id": 2, "label": "Group"}
]
```
2. **Получение узла и его связей**
- **URL:** `/node/{node_id}`
- **Метод:** `GET`
- **Описание:** Возвращает узел, его связи и связанные узлы.
- **Пример ответа:**
```json
[
    {"n": {"id": 1, "name": "John Doe"}, "r": {"type": "Follow"}, "m": {"id": 2, "name": "Jane Doe"}}
]
```
3. **Добавление узла и связей**
- **URL:** `/insert`
- **Метод:** `POST`
- **Авторизация:** Требуется токен в заголовке `Authorization`.
- **Описание:** Создает узел и добавляет связи.
- **Тело запроса:**
```json
{
    "node": {
        "id": 3,
        "label": "User",
        "name": "Jane Doe",
        "screen_name": "janedoe",
        "sex": 2,
        "home_town": "San Francisco"
    },
    "relationships": [
        {"id": 20, "type": "Follow", "end_node_id": 1}
    ]
}
```
- **Пример ответа:**
```json
{"status": "Node and relationships added"}
```
4. **Удаление узла и связей**
- **URL:** `/node/{node_id}`
- **Метод:** `DELETE`
- **Авторизация:** Требуется токен в заголовке `Authorization`.
- **Описание:** Удаляет узел и все его связи.
- **Пример ответа:**
```json
{"status": "Node 3 and its relationships deleted"}
```
## Тестирование
Запуск тестов
Для тестирования используется `pytest`. Запустите тесты командой:

```bash
pytest
```
**Тестируемые сценарии:**
1. Проверка получения всех узлов.
2. Проверка получения узла и его связей.
3. Проверка добавления узла и связей.
4. Проверка удаления узла и связей.

## Используемые технологии
- `FastAPI` — разработка API.
- `Neo4j` — графовая база данных.
- `Py2Neo` — Python-клиент для работы с Neo4j.
- `Pydantic` — работа с моделями данных.
- `Uvicorn` — сервер ASGI.