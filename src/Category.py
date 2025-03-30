from src.Products import Product,Smartphone,LawnGrass
class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if isinstance(product,(Product,Smartphone,LawnGrass)):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_list(self):
        products_str = ""
        for i in self.__products:
            products_str = f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт."
        return products_str

    @property
    def products(self):
        return self.__products

