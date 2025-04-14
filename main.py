
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from models import WalletQuery, Base
from schemas import WalletQueryResponse, WalletQueryCreate
from services import get_wallet_info
from database import get_db, engine

# Создаём таблицы в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/wallet-info/")
def get_wallet_info_post(wallet_query: WalletQueryCreate, db: Session = Depends(get_db)):
    wallet_data = get_wallet_info(wallet_query.address)
    if wallet_data is None:
        raise HTTPException(status_code=404, detail="Address not found")
    
    wallet_query_db = WalletQuery(
        address=wallet_query.address,
        trx_balance=wallet_data["trx_balance"],
        bandwidth=wallet_data["bandwidth"],
        energy=wallet_data["energy"]
    )
    db.add(wallet_query_db)
    db.commit()
    db.refresh(wallet_query_db)
    return wallet_query_db

@app.get("/wallet-info/", response_model=List[WalletQueryResponse])
def get_wallet_info_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    wallet_queries = db.query(WalletQuery).offset(skip).limit(limit).all()
    return wallet_queries
