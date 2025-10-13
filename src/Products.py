from abc import ABC, abstractmethod


class LoggingMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        # Вызываем __init__ родительского класса
        super().__init__(*args, **kwargs)

        # Получаем имя класса
        class_name = self.__class__.__name__

        # Формируем строку с параметрами
        params = []

        # Обрабатываем позиционные аргументы (первые 4 - основные параметры Product)
        if len(args) >= 1:
            params.append(f"name='{args[0]}'")
        if len(args) >= 2:
            params.append(f"description='{args[1]}'")
        if len(args) >= 3:
            params.append(f"price={args[2]}")
        if len(args) >= 4:
            params.append(f"quantity={args[3]}")

            # Обрабатываем именованные аргументы
            for key, value in kwargs.items():
                if isinstance(value, str):
                    params.append(f"{key}='{value}'")
                else:
                    params.append(f"{key}={value}")

            # Выводим информацию о создании объекта
            print(f"Создан объект {class_name}({', '.join(params)})")


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, added_product: dict, product_list: list):
        pass


class Product(LoggingMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        # Инициализируем атрибуты напрямую, не передавая лишние аргументы
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        # Вызываем __init__ миксина после установки атрибутов
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, added_product: dict, product_list: list):
        for product in product_list:
            if product.name == added_product["name"]:
                product.quantity += added_product["quantity"]
                product.price = max(product.price, added_product["price"])
                return product

        new_product = cls(
            name=added_product["name"],
            description=added_product["description"],
            price=added_product["price"],
            quantity=added_product["quantity"]
        )
        product_list.append(new_product)
        return new_product

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self._price:
            confirmation = input(f"Цена понижается с {self._price} до {new_price}. Вы уверены? (y/n): ")
            if confirmation.lower() == 'y':
                self._price = new_price
                print(f"Цена обновлена на {new_price}")
            else:
                print("Изменение цены отменено.")
        else:
            self._price = new_price

    def __add__(self, other):
        if type(other) == self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        # Сначала инициализируем основные атрибуты через родительский класс
        super().__init__(name, description, price, quantity)
        # Затем устанавливаем специфичные атрибуты
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        # Сначала инициализируем основные атрибуты через родительский класс
        super().__init__(name, description, price, quantity)
        # Затем устанавливаем специфичные атрибуты
        self.country = country
        self.germination_period = germination_period
        self.color = color


