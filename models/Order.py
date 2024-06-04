from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship

from models.database import Base

#association_table = Table('Order_association', Base.metadata,
#                          Column('Order_ID', Integer, ForeignKey('Order.id')),
#                          Column('Payment_ID', Integer, ForeignKey('Payment.id')),
#                          Column('Basket_ID',Integer, ForeignKey('Basket.id'))
#                          )


class Order(Base):
    __tablename__ = 'Order'

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer, ForeignKey('Client.id'))

    payment_id = relationship('Payment', uselist=False)

    basket_id = relationship('Basket', uselist=False)

    order_date = Column(Integer, nullable=False)

    def __init__(self,  client_id: int, order_date: int):
        self.client_id = client_id
        self.order_date = order_date

    def __repr__(self):
        return (f'Заказ [ID: {self.id}, ID_Клиента: {self.client_id}, ID_Платежа: {self.payment_id}, ID_Корзины: '
                f'{self.basket_id}]')
