from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.database import Base


class Client(Base):
    __tablename__ = 'Client'

    id = Column(Integer, primary_key=True)
    order_id = relationship('Order')
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address = Column(String)
    discount = Column(Integer)

    def __init__(self,  first_name: str, last_name: str, email: str, address: str, discount: int):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.discount = discount

    def __repr__(self):
        info: str = f'Клиент [ФамилияИмя: {self.first_name} {self.last_name}, ' \
                    f'Email: {self.email}, Адрес: {self.address}, Скидка: {self.discount}]'
        return info
