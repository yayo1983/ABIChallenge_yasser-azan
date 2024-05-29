from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Customer(Base):
    
    __tablename__ = "customer"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    invoice = Column(String)
    stock_code = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    invoice_date = Column(String)
    price = Column(Float)
    country = Column(String)