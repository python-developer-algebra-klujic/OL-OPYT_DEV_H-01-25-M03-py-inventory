from sqlalchemy import Column, Integer, String, Float, ForeignKey

from constants import (NAME_LENGTH, CODE_LENGTH,
                       Base)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=NAME_LENGTH), nullable=False, default='No name')
    code = Column(String(length=CODE_LENGTH), nullable=False, default='NN')
    price = Column(Float(), nullable=False, default=0.0)
    category_id = Column(Integer, ForeignKey('categories.id'))

    def __repr__(self):
        return f'Product: {self.name} ({self.code})'
