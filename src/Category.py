from src.Products import BaseProduct, Product, Smartphone, LawnGrass
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
    def __str__(self):
        quantity=0
        for i in self.__products:
            quantity+=i.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."
    def add_product(self, product):
        if isinstance(product,(Product,Smartphone,LawnGrass)):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        return self.__products


