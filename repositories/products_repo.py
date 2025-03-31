from typing import List

from sqlalchemy import and_, or_

from constants import session
from models import Product


class ProductsRepo:
    def __init__(self):
        self.session = session

    def get_products(self) -> List[Product]:
        try:
            return (self.session
                        .query(Product)
                        .all())
        except Exception as ex:
            print(f'Dogodila se greska u "get_products()": {ex}')
            return []


    def get_product(self, id: int) -> Product:
        try:
            return (self.session
                        .query(Product)
                        .filter(Product.id == id)
                        .one_or_none())
        except Exception as ex:
            print(f'Dogodila se greska u "get_product()": {ex}')
            return None


    def create_product(self, product: Product) -> Product:
        try:
            product_from_db = (self.session
                                    .query(Product)
                                    .filter(
                                        and_(
                                            Product.name == product.name,
                                            Product.code == product.code
                                        )
                                    ).one_or_none())

            if product_from_db == None:
                self.session.add(product)
                return product

            return product_from_db

        except Exception as ex:
            print(f'Dogodila se greska u "create_product()": {ex}')
            return None


    def update_product(self, product: Product) -> Product:
        try:
            product_from_db = (self.session
                                    .query(Product)
                                    .filter(
                                        Product.id == product.id
                                    ).one_or_none())

            if product_from_db != None:
                product_from_db = product

            return product_from_db
        except Exception as ex:
            print(f'Dogodila se greska u "update_product()": {ex}')
            return None


    def delete_product(self, id: int) -> None:
        try:
            product_from_db = (self.session
                                    .query(Product)
                                    .filter(
                                        Product.id == id
                                    ).one_or_none())
            self.session.delete(product_from_db)
        except Exception as ex:
            print(f'Dogodila se greska u "delete_product()": {ex}')

        return None

    def db_commit(self):
        self.session.commit()
