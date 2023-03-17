from datetime import datetime
from enum import Enum
from typing import List, Optional
from urllib.request import Request

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, ValidationError
from starlette import status
from starlette.responses import JSONResponse

from operations.router import router as router_operation
from trades.router import router as router_trade
from operations.router import arr


app = FastAPI(
    title = "Test api"
)

all_trades = [{"id":1 ,"user_id" : 1,"currency":"BTC", "price" : 100},
              {"id":2 ,"user_id" : 2,"currency":"BTC", "price" : 200},
              {"id":3 ,"user_id" : 1,"currency":"Sber", "price" : 300}]

@app.get("/")


def get_hello():
    return arr



@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


users = [{"id":1 , "name":["Bob"]},
         {"id":2 ,"name":"Jon"},
         {"id":3 , "name":"Sara"},
         {"id":4 , "name":"Alex", "degree":[
             {"id":1 , "created_at":"2020-01-01T00:00:00","type_degree":"expert"}
    ]}
]


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id : int
    created_at : datetime
    type_degree : DegreeType


class User(BaseModel):
    id : int
    name : str
    degree : Optional[List[Degree]] = "no degree"

@app.get("/users/{user_id}", response_model=List[User])
def get_users(user_id : int):
    return [user for user in users if user.get("id") == user_id]


@app.post("/users/{user_id}")

def rename_user(user_id:int, new_name:str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users))[0]
    current_user["name"] = new_name
    return {"status":200 , "data":current_user}


# all_trades = [{"id":1 ,"user_id" : 1,"currency":"BTC", "price" : 100},
#               {"id":2 ,"user_id" : 2,"currency":"BTC", "price" : 200},
#               {"id":3 ,"user_id" : 1,"currency":"Sber", "price" : 300}]


# class Trade(BaseModel):
#     id : int
#     user_id : int
#     currency : str = Field(max_length=5)
#     price : float = Field(ge=0)
#
# @app.post("/trades")
# def add_trades(trades : list[Trade]):
#     all_trades.extend(trades)
#     return {"status":200 , "data": all_trades}

app.include_router(router_operation)

app.include_router(router_trade)