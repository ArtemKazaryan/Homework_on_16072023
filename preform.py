from sqlalchemy import func

from models.models import Sales, Salesmen, Customers

from models.database import Session
from decoration import save_results_to_file

session = Session()


@save_results_to_file
def all_items(name_table):
    return session.query(name_table)


@save_results_to_file
def sales_by_salesman(id: int):
    result = session.query(Sales.date,
                           Sales.amount,
                           Customers.name,
                           Salesmen.name) \
        .join(Salesmen, Sales.salesman_id == Salesmen.id) \
        .join(Customers, Sales.customer_id == Customers.id) \
        .filter(Salesmen.id == id) \
        .all()
    return result


@save_results_to_file
def max_value():
    result = session.query(Sales.id, func.max(Sales.amount)).all()
    return result


@save_results_to_file
def min_value():
    result = session.query(Sales.id, func.min(Sales.amount)).all()
    return result


@save_results_to_file
def max_sale_by_salesman(id: int):
    result = session.query(Sales.amount, func.max(Sales.amount)) \
        .join(Salesmen, Sales.salesman_id == Salesmen.id).filter(Salesmen.id == id).first()[0]
    return result


@save_results_to_file
def min_sale_by_salesman(id: int):
    result = session.query(Sales.amount, func.min(Sales.amount)) \
        .join(Salesmen, Sales.salesman_id == Salesmen.id).filter(Salesmen.id == id).first()[0]
    return result


@save_results_to_file
def max_sale_by_customers(id: int):
    result = session.query(Sales.amount, func.max(Sales.amount)) \
        .join(Customers, Sales.salesman_id == Customers.id).filter(Customers.id == id).first()[0]
    return result


@save_results_to_file
def min_sale_by_customers(id: int):
    result = session.query(Sales.amount, func.min(Sales.amount)) \
        .join(Customers, Sales.salesman_id == Customers.id).filter(Customers.id == id).first()[0]
    return result


@save_results_to_file
def max_sale_by_all_salesmen():
    result = session.query(Salesmen, func.sum(Sales.amount)) \
        .join(Sales, Sales.salesman_id == Salesmen.id) \
        .group_by(Sales.salesman_id) \
        .order_by(func.sum(Sales.amount).desc()) \
        .first()
    return result


@save_results_to_file
def min_sale_by_all_salesmen():
    result = session.query(Salesmen, func.sum(Sales.amount)) \
        .join(Sales, Sales.salesman_id == Salesmen.id) \
        .group_by(Sales.salesman_id) \
        .order_by(func.sum(Sales.amount)) \
        .first()
    return result


@save_results_to_file
def max_sale_by_all_customers():
    result = session.query(Customers, func.sum(Sales.amount)) \
        .join(Sales, Sales.customer_id == Customers.id) \
        .group_by(Sales.customer_id) \
        .order_by(func.sum(Sales.amount).desc()) \
        .first()
    return result


@save_results_to_file
def avg_sale_by_salesman():
    result = session.query(Salesmen, func.avg(Sales.amount)) \
        .join(Sales, Sales.salesman_id == Salesmen.id) \
        .filter(Sales.salesman_id == id) \
        .first()
    return result


@save_results_to_file
def avg_sale_by_customers(id: int):
    result = session.query(Customers, func.avg(Sales.amount)) \
        .join(Sales, Sales.customer_id == Customers.id) \
        .filter(Sales.customer_id == id) \
        .first()
    return result


def key_request(name_table, id):
    result = session.get(name_table, id)
    return result


def update_sale(sale_id, salesman_id, customer_id, amount):
    user_query = session.query(Sales).filter_by(id=sale_id)
    date_to_update = dict(salesman_id=salesman_id, customer_id=customer_id, amount=amount)
    user_query.update(date_to_update)
    session.commit()


def update_customers(customers_id, name):
    user_query = session.query(Customers).filter_by(id=customers_id)
    date_to_update = dict(name=name)
    user_query.update(date_to_update)
    session.commit()


def update_salesman(salesmen_id, name):
    user_query = session.query(Salesmen).filter_by(id=salesmen_id)
    date_to_update = dict(name=name)
    user_query.update(date_to_update)
    session.commit()


def insert_table(value):
    session.add(value)
    session.commit()


def delete_entry(value):
    session.delete(value)
    session.commit()
