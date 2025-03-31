from constants import Base, engine
from repositories import DbSeeder
from UI import list_categories_w_products, list_categories_wo_products


def main():
    list_categories_wo_products()
    print()
    list_categories_w_products()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    db_seeder = DbSeeder()
    db_seeder.seed_db()

    main()
