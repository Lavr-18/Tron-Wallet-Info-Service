
from pydantic import BaseModel
from typing import List, Optional

class WalletQueryResponse(BaseModel):
    address: str
    trx_balance: float
    bandwidth: int
    energy: int
    created_at: str

    class Config:
        orm_mode = True

class WalletQueryCreate(BaseModel):
    address: str
