from pydantic import BaseModel, Field


class Trade(BaseModel):
    id : int
    user_id : int
    currency : str = Field(max_length=5)
    price : float = Field(ge = 0)