from repositories import ProductCategoriesRepo


def list_categories_wo_products() -> None:
    product_categories_repo = ProductCategoriesRepo()
    for product_category in product_categories_repo.get_product_categories():
        print()
        print('CATEGORY', end='\t')
        print(product_category)
        print()
