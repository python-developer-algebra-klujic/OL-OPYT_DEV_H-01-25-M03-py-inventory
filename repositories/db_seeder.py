from models import Product, ProductCategory
from repositories import ProductCategoriesRepo, ProductsRepo
from constants import INVENTORY_SEED as inventory


class DbSeeder:
    def __init__(self):
        self.product_repo = ProductsRepo()
        self.category_repo = ProductCategoriesRepo()

    def seed_db(self):
        for category_name, products in inventory.items():
            category = ProductCategory(
                name=category_name
            )
            category = self.category_repo.create_product_category(category)
            if category != None:
                for product_list in products:
                    product = Product(
                        name=product_list['name'],
                        code=product_list['code'],
                        price=product_list['price']
                    )
                    product.category = category
                    self.product_repo.create_product(product)
            else:
                continue
        self.category_repo.db_commit()
        self.product_repo.db_commit()
