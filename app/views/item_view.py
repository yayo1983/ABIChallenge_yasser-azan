
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.models.customer import Customer
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
from pandas import DataFrame
from app.database import engine

class ItemView:
    
    def __init__(self, db: Session):
        """
        Initializes the Item instance with a database session.

        Args:
            db (Session): The database session to be used for operations.
        """
        self.db = db
    
    @staticmethod
    def display_item(item):
        item_dict = item.dict()
        return JSONResponse(content=item_dict)
    
    def save_items(self, df: DataFrame):
        """
        save  the customer
        """
        try:
            
            for index, row in df.iterrows():
                item = Customer(
                    customer_id = pd.to_numeric(row['Customer ID'], errors="coerce"),
                    invoice = row['Invoice'],
                    stock_code = row['StockCode'],
                    description = row['Description'],
                    quantity = pd.to_numeric(row['Quantity'], errors="coerce"),
                    invoice_date = row['InvoiceDate'],
                    price = pd.to_numeric(row['Price'], errors="coerce") ,
                    country = row['Country']
                    )
                print("el objeto", row['StockCode'])
                self.db.add(item)
            self.db.commit()
            return True
        except SQLAlchemyError as e:
           self.db.rollback()
           print("Error in save items", e)
        except Exception as e:
           print("Error in save items", e)
           return False
        
    def get_data(self):
        query = "SELECT * FROM customer"
        try:  
            df = pd.read_sql(query, engine)
            return df
        except SQLAlchemyError as e:
           print("Error in unique_variables function, read database", e)
        return False
    
    def unique_variables(self):
        df = self.get_data()
        if df is False:
            return False
        unique_counts = df.nunique()
        print("unique_counts", unique_counts)
        return unique_counts
    
    def count_by_product(self):
        """
        Examining how many of each product are
        """
        df = self.get_data()
        if df is False:
            return False
        count_product  = df["description"].value_counts()
        print("count_product" , count_product )
        return count_product
        
            
        