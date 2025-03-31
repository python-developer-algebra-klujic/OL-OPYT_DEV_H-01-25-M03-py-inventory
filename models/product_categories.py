from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from constants import (NAME_LENGTH, Base)


class ProductCategory(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=NAME_LENGTH), nullable=False, default='No name')

    products = relationship('Product', backref=backref('category'))

    def __repr__(self):
        return f'Category: {self.name}'
