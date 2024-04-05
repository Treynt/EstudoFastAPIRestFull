from typing import List
from uuid import uuid4
from fastapi import FastAPI

from projeto.models import User, Gender, Role

app = FastAPI()

#criação do database por lista, no exemplo, mas pode associar com um real
db: List[User] = [
    User(
        id = uuid4(),
        first_name= "Jamila",
        last_name= "Ahmed",
        gender= Gender.female,
        roles=[Role.student]
    )
]


@app.get("/")
def root():
    return {"Hello": "World"}