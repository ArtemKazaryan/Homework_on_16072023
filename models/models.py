import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DATE

from .database import Base


class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    date = Column(DATE, default=datetime.date.year)
    salesman_id = Column(Integer, ForeignKey('salesmen.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    amount = Column(Integer)

    def __repr__(self):
        return f"id: {self.id}, " \
               f"date: {self.date}, " \
               f"salesman_id: {self.salesman_id}, " \
               f"customer_id: {self.customer_id}, " \
               f"amount: {self.amount};"


class Salesmen(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"id: {self.id}, name: {self.name};"


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"id: {self.id}, name: {self.name};"