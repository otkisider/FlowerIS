from faker import Faker
from models.database import create_db, Session
from models.Client import Client
from models.Order import Order
from models.Payment import Payment
from models.Basket import Basket
from models.Product import Product


def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session: Session):
    faker = Faker('ru-RU')
    session.commit()

    client_num = 50
    store_num = 5

    for _ in range(client_num):
        first_name = faker.first_name_male()
        last_name = faker.last_name_male()
        email = faker.email()
        address = faker.address()
        discount = faker.random.randint(5, 20)
        client = Client(first_name, last_name, email, address, discount)

        session.add(client)

        session.commit()
        session.close()

    for _ in range(20):
        store_id = faker.random.randint(1, store_num)
        basket_id = faker.random.randint(1, client_num)
        product_name = faker.bothify('Product: ????-######')
        store_opening_time = faker.time()

        product = Product(store_id, basket_id, product_name, store_opening_time)

        session.add(product)

        session.commit()
        session.close()

    for _ in range(client_num):
        client_id = faker.random.randint(1, client_num)
        order_date = faker.time()

        order = Order(client_id, order_date)
        session.add(order)

        session.commit()
        session.close()

# Переименовать переменные, сделать API, оформить отчет
