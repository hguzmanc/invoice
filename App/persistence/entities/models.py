from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from App import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Sales(db.Model):
    __table_name__ = "sales"
    id = Column(Integer, primary_key=True, nullable=False)
    nit_client = Column(String(10), nullable=False)
    name_client = Column(String(100), nullable=False)

    def __init__(self, nit, name):
        self.nit = nit
        self.name = name

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)


class Invoice(db.Model):
    __table_name__ = "invoice"
    id = Column(Integer, primary_key=True, nullable=False)
    nit_invoice = Column(String(10), nullable=False)
    number_invoice = Column(String(10), nullable=False)
    number_authorization = Column(String(10), nullable=False)
    date_invoice = Column(DateTime, nullable=False)
    id_sales = Column(Integer, ForeignKey('sales.id'), nullable=False)

    def __init__(self, nit_invoice, number_invoice, number_authorization, date_invoice, id_client):
        self.nit_invoice = nit_invoice
        self.number_invoice = number_invoice
        self.number_authorization = number_authorization
        self.date_invoice = date_invoice
        self.id_client = id_client

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)


class Product(db.Model):
    __table_name__ = "product"
    id = Column(Integer, primary_key=True, nullable=False)
    name_product = Column(String(80), nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self, name_product, price):
        self.name_product = name_product
        self.price = price

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)


class DetailSales(db.Model):
    __table_name__ = "detail_product_invoice"
    id = Column(Integer, primary_key=True, nullable=False)
    id_sales = Column(Integer, ForeignKey('sales.id'), nullable=False)
    id_product = Column(Integer, ForeignKey('product.id'), nullable=False)
    product_quantity = Column(Float, nullable=False)

    def __init__(self, id_sales, id_product, product_quantity):
        self.id_invoice = id_sales
        self.id_product = id_product
        self.product_quantity = product_quantity

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)
