from constants import Base, engine
from repositories import DbSeeder


def main():
    # Pokreni aplikaciju
    print('main() is working')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    db_seeder = DbSeeder()
    db_seeder.seed_db()

    main()
