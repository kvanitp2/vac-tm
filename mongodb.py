from pymongo import MongoClient
from settings import MONGO_URL, MONGO_DB
mdb = MongoClient(MONGO_URL)[MONGO_DB]

def get_vacancies():
    return mdb.vac.find()


# название, зарплата, описание, телефон

# to_add = {"title":"Почтальон", "salary":"17000", "description": "Разносить", "phone": "+79129992233"}
# mdb.vac.insert_one(to_add)  