from pydantic import Field

from fastapi import APIRouter
from pydantic import BaseModel

from schemes.schemes import Trade

router = APIRouter(
    prefix = "/trades",
    tags = ["Trade"]
)


all_trades = [{"id":1 ,"user_id" : 1,"currency":"BTC", "price" : 100},
              {"id":2 ,"user_id" : 2,"currency":"BTC", "price" : 200},
              {"id":3 ,"user_id" : 1,"currency":"Sber", "price" : 300}]

# class Trade(BaseModel):
#     id : int
#     user_id : int
#     currency : str = Field(max_length=5)
#     price : float = Field(ge = 0)

@router.post("/")
async def add_trades(trades : list[Trade]):
    all_trades.extend(trades)
    return {"status":200 , "data": all_trades}


@router.get("/{trade_id}")

async def get_trades(trade_id : int):
    return {"status: 200","price = " + str(*[trade.get("price") for trade in all_trades if trade.get("id") == trade_id])}


@router.delete("/{trade_id}")

async def del_trades(trade_id : int):
    [all_trades.remove(tr) for tr in all_trades if tr.get("id") == trade_id]
    return {"status" : 200,"data" : all_trades}