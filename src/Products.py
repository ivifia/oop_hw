from abc import ABC, abstractmethod


class LoggingMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        # Сохраняем аргументы для логирования
        self._init_args = args
        self._init_kwargs = kwargs
        # Вызываем __init__ родительского класса только с основными аргументами
        super().__init__(*args[:4])  # Передаем только name, description, price, quantity
        # Логируем после инициализации
        self._log_creation()

    def _log_creation(self):
        """Логирует создание объекта"""
        class_name = self.__class__.__name__

        # Формируем строку с параметрами
        params = []

        # Обрабатываем позиционные аргументы (первые 4)
        if len(self._init_args) >= 1:
            params.append(f"name='{self._init_args[0]}'")
        if len(self._init_args) >= 2:
            params.append(f"description='{self._init_args[1]}'")
        if len(self._init_args) >= 3:
            params.append(f"price={self._init_args[2]}")
        if len(self._init_args) >= 4:
            params.append(f"quantity={self._init_args[3]}")

        # Обрабатываем именованные аргументы (дополнительные параметры)
        for key, value in self._init_kwargs.items():
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
    def __init__(self, name, description, price, quantity, **kwargs):
        # Проверяем количество товара
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        # Передаем все аргументы в миксин
        super().__init__(name, description, price, quantity, **kwargs)

    @classmethod
    def new_product(cls, added_product: dict, product_list: list):
        # Проверяем количество при создании нового товара
        if added_product["quantity"] == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        for product in product_list:
            if product.name == added_product["name"]:
                # При обновлении существующего товара проверяем, чтобы общее количество не стало нулевым
                new_quantity = product.quantity + added_product["quantity"]
                if new_quantity == 0:
                    raise ValueError("Товар с нулевым количеством не может быть добавлен")

                product.quantity = new_quantity
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
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Можно складывать только продукты")


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        # Передаем все параметры в родительский конструктор
        super().__init__(name, description, price, quantity,
                         efficiency=efficiency, model=model, memory=memory, color=color)


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        # Передаем все параметры в родительский конструктор
        super().__init__(name, description, price, quantity,
                         country=country, germination_period=germination_period, color=color)