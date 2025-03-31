from constants import session
from models import Product, ProductCategory


class DbSeeder:
    def __init__(self):
        self.session = session

    def seed_db(self):
        racunalna_periferija = ProductCategory(
            name='Racunalna periferija'
        )
        self.session.add(racunalna_periferija)

        monitor = Product(
            name='Monitor',
            code='MNT',
            price=599.123
        )
        monitor.category = racunalna_periferija
        self.session.add(monitor)
        self.session.commit()
