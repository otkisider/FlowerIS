from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from models.database import Base

#association_table = Table('Basket_association', Base.metadata,
#                          Column('Basket_ID', Integer, ForeignKey('Basket.id')),
#                          Column('Product_ID', Integer, ForeignKey('Product.id')),
#                          Column('Order_ID', Integer, ForeignKey('Order.id'))
#                          )


class Basket(Base):
    __tablename__ = 'Basket'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('Order.id'))
    product_name = Column(String)
    product_id = relationship('Product')

    def __init__(self,  order_id: int, product_name: int, product_id: int):
        self.order_id = order_id
        self.product_name = product_name
        self.product_id = product_id

    def __repr__(self):
        return f'Корзина [ID: {self.id}, Название_продукта: {self.product_name}, ID_Продукта: {self.product_id}]'
