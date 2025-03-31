from typing import List

from constants import session
from models import ProductCategory


class ProductCategoriesRepo:
    def __init__(self):
        self.session = session

    def get_product_categories(self) -> List[ProductCategory]:
        try:
            return (self.session
                        .query(ProductCategory)
                        .all())
        except Exception as ex:
            print(f'Dogodila se greska u "get_product_categories()": {ex}')
            return []


    def get_product_category(self, id: int) -> ProductCategory:
        try:
            return (self.session
                        .query(ProductCategory)
                        .filter(ProductCategory.id == id)
                        .one_or_none())
        except Exception as ex:
            print(f'Dogodila se greska u "get_product_category()": {ex}')
            return None


    def create_product_category(self, product_category: ProductCategory) -> ProductCategory:
        try:
            product_category_from_db = (self.session
                                            .query(ProductCategory)
                                            .filter(
                                                ProductCategory.name == product_category.name,
                                            ).one_or_none())

            if product_category_from_db == None:
                self.session.add(product_category)
                return product_category

            return product_category_from_db

        except Exception as ex:
            print(f'Dogodila se greska u "create_product_category()": {ex}')
            return None


    def update_product_category(self, product_category: ProductCategory) -> ProductCategory:
        try:
            product_category_from_db = (self.session
                                    .query(ProductCategory)
                                    .filter(
                                        ProductCategory.id == product_category.id
                                    ).one_or_none())

            if product_category_from_db != None:
                product_category_from_db = product_category

            return product_category_from_db
        except Exception as ex:
            print(f'Dogodila se greska u "update_product_category()": {ex}')
            return None


    def delete_product_category(self, id: int) -> None:
        try:
            product_category_from_db = (self.session
                                    .query(ProductCategory)
                                    .filter(
                                        ProductCategory.id == id
                                    ).one_or_none())
            self.session.delete(product_category_from_db)
        except Exception as ex:
            print(f'Dogodila se greska u "delete_product_category()": {ex}')

        return None

    def db_commit(self):
        self.session.commit()
