
from faker import Faker
from models.database import create_db, Session
from models.models import Sales, Salesmen, Customers

fake = Faker('ru-RU')


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    # Заполнение таблиц Salesmen, Customers, Sales
    for _ in range(5):
        # Заполнение таблицы Salesmen
        name = fake.company()
        salesman = Salesmen(name=name)
        session.add(salesman)

    for _ in range(20):
        # Заполнение таблицы Customers
        name = fake.name()
        customer = Customers(name=name)
        session.add(customer)

    for _ in range(50):
        # Заполнение таблицы Sales
        salesman_id = fake.random_int(min=1, max=5)
        customer_id = fake.random_int(min=1, max=20)
        date = fake.date_between(start_date='-3y', end_date='today')
        amount = fake.random_int(min=10, max=10000)
        sale = Sales(date=date, salesman_id=salesman_id, customer_id=customer_id, amount=amount)
        session.add(sale)

    session.commit()
    print("база данных создана")
    session.close()