
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class WalletQuery(Base):
    __tablename__ = 'wallet_queries'

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    trx_balance = Column(Float)
    bandwidth = Column(Integer)
    energy = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
