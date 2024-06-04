from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship

from models.database import Base

#association_table = Table('Product_association', Base.metadata,
#                          Column('Product_ID', Integer, ForeignKey('Product.id')),
#                          Column('Basket_ID', Integer, ForeignKey('Basket.id'))
#                          )


class Product(Base):
    __tablename__ = 'Product'

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer)
    basket_id = Column(Integer, ForeignKey('Basket.id'))
    product_name = Column(String)
    store_opening_time = Column(Integer)

    def __init__(self, store_id: int, basket_id: int, product_name: str, store_opening_time: int):
        self.store_id = store_id
        self.basket_id = basket_id
        self.product_name = product_name
        self.store_opening_time = store_opening_time


    def __repr__(self):
        return (f'Магазин [ID: {self.id}, ID_Продукта; {self.product_id}, Название_Продукта; {self.product_name}, '
                f'Время_открытия_магазина: {self.store_opening_time}]')
