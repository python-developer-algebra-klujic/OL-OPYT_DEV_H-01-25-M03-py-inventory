from constants import Base, engine
from repositories import DbSeeder, ProductCategoriesRepo


def main():
    # Pokreni aplikaciju
    product_categories_repo = ProductCategoriesRepo()
    for product_category in product_categories_repo.get_product_categories():
        print()
        print('CATEGORY', end='\t')
        print(product_category)
        print('PRODUCTS:')
        for index, product in enumerate(product_category.products):
            print(f'{index + 1}.{'\t'}{product}')
        print()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    db_seeder = DbSeeder()
    db_seeder.seed_db()

    main()
