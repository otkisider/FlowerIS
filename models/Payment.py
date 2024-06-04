from sqlalchemy import Column, Integer, String, Table, ForeignKey

from models.database import Base

#association_table = Table('Payment_association', Base.metadata,
#                          Column('Payment_ID', Integer, ForeignKey('Payment.id')),
#                          Column('Order_ID', Integer, ForeignKey('Order.id'))
#                          )


class Payment(Base):
    __tablename__ = 'Payment'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('Order.id'))
    type = Column(String)
    status = Column(String)
    payment_amount = Column(Integer)

    def __repr__(self):
        return f'Оплата [ID: {self.id}, Тип: {self.type}, Статус: {self.status}, Оплачено; {self.payment_amount}]'
