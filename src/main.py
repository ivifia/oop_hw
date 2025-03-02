class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, added_product: dict, product_list: list):
        for product in product_list:
            if product.name == added_product["name"]:
                product.quantity += added_product["quantity"]

                product.check_price = max(product.check_price, added_product["price"])
                return product


        new_product = cls(
            name=added_product["name"],
            price=added_product["price"],
            description=added_product["description"],
            quantity=added_product["quantity"]
        )
        product_list.append(new_product)
        return new_product

    @property
    def check_price(self):
        return self.__price
    @check_price.setter
    def check_price(self,new_price):
        if new_price<=0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirmation = input(f"Цена понижается с {self.__price} до {new_price}. Вы уверены? (y/n): ")
            if confirmation.lower() == 'y':
                self.__price = new_price
                print(f"Цена обновлена на {new_price}")
            else:
                print("Изменение цены отменено.")
        else:
            self.__price=new_price



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
        self.__products.append(product)
        Category.category_count += 1
        Category.product_count += 1

    @property
    def products_list(self):
        products_str = ""
        for i in self.__products:
            products_str = f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт."
        return products_str