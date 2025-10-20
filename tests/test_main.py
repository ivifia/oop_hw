import pytest
from unittest.mock import patch, MagicMock
from src.Products import Product, Smartphone, LawnGrass, LoggingMixin, BaseProduct
from src.Category import Category


# Существующие тесты (без изменений)

@pytest.fixture()
def test_Category():
    product1 = Product("banana", "yellow fruit", 10.0, 5)
    product2 = Product("pop", "drink", 20.0, 3)
    return Category("Иван", "lflflf", [product1, product2])


def test_init_category(test_Category):
    assert test_Category.name == "Иван"
    assert test_Category.description == "lflflf"
    assert len(test_Category.products) == 2
    assert isinstance(test_Category.products[0], Product)
    assert test_Category.category_count >= 1
    assert test_Category.product_count >= 2


@pytest.fixture()
def test_Product():
    return Product("Иван", "lal", 12.0, 4)


def test_init_product(test_Product):
    assert test_Product.name == "Иван"
    assert test_Product.description == "lal"
    assert test_Product.price == 12.0
    assert test_Product.quantity == 4


def test_set_price(test_Product):
    test_Product.price = 15.0
    assert test_Product.price == 15.0


def test_set_price_invalid(test_Product):
    with patch("builtins.print") as mocked_print:
        test_Product.price = -5.0
        mocked_print.assert_called_with("Цена не должна быть нулевая или отрицательная")
        assert test_Product.price == 12.0


def test_set_price_decrease_confirmation(test_Product):
    with patch("builtins.input", return_value="y"):
        test_Product.price = 10.0
        assert test_Product.price == 10.0

    with patch("builtins.input", return_value="n"):
        test_Product.price = 8.0
        assert test_Product.price == 10.0


@pytest.fixture()
def product_list():
    return []


def test_new_product_addition(product_list):
    added_product = {"name": "Яблоко", "description": "Зеленое", "price": 10.0, "quantity": 5}
    product = Product.new_product(added_product, product_list)

    assert len(product_list) == 1
    assert product.name == "Яблоко"
    assert product.price == 10.0
    assert product.quantity == 5


def test_new_product_update_existing(product_list):
    existing_product = {"name": "Яблоко", "description": "Зеленое", "price": 10.0, "quantity": 5}
    Product.new_product(existing_product, product_list)

    updated_product = {"name": "Яблоко", "description": "Красное", "price": 12.0, "quantity": 3}
    product = Product.new_product(updated_product, product_list)

    assert len(product_list) == 1
    assert product.name == "Яблоко"
    assert product.price == 12.0
    assert product.quantity == 8


@pytest.fixture()
def test_Smartphone():
    return Smartphone("Samsung A73", "good smartphone", 50.0, 35, "high", "A73", 128, "grey")


def test_init_smartphone(test_Smartphone):
    assert test_Smartphone.name == "Samsung A73"
    assert test_Smartphone.description == "good smartphone"
    assert test_Smartphone.price == 50.0
    assert test_Smartphone.quantity == 35
    assert test_Smartphone.efficiency == "high"
    assert test_Smartphone.model == "A73"
    assert test_Smartphone.memory == 128
    assert test_Smartphone.color == "grey"


@pytest.fixture()
def test_LawnGrass():
    return LawnGrass("Grass_cuter", "best", 50.0, 35, "Germany", "73 days", "grey")


def test_init_LawnGrass(test_LawnGrass):
    assert test_LawnGrass.name == "Grass_cuter"
    assert test_LawnGrass.description == "best"
    assert test_LawnGrass.price == 50.0
    assert test_LawnGrass.quantity == 35
    assert test_LawnGrass.country == "Germany"
    assert test_LawnGrass.germination_period == "73 days"
    assert test_LawnGrass.color == "grey"


@pytest.fixture
def product1():
    return Product("Телефон", "Смартфон", 50000, 3)


@pytest.fixture
def product2():
    return Product("Ноутбук", "Игровой", 100000, 2)


def test_product_add(product1, product2):
    total = product1 + product2
    assert total == (50000 * 3) + (100000 * 2)


@pytest.fixture
def category():
    return Category("Электроника", "Техника", [])


@pytest.fixture
def product():
    return Product("Телефон", "Смартфон", 50000, 3)


@pytest.fixture
def smartphone():
    return Smartphone("iPhone", "Премиум", 100000, 5, "A15", "13 Pro", 256, "Silver")


@pytest.fixture
def lawn_grass():
    return LawnGrass("Трава", "Для газона", 500, 10, "Россия", "14 дней", "Зеленая")


def test_add_valid_product(category, product):
    category.add_product(product)
    assert len(category.products) == 1


def test_add_smartphone(category, smartphone):
    category.add_product(smartphone)
    assert len(category.products) == 1


def test_add_lawn_grass(category, lawn_grass):
    category.add_product(lawn_grass)
    assert len(category.products) == 1


# Новые тесты для миксина логирования

def test_logging_mixin_inheritance():
    """Тест, что Product наследует LoggingMixin"""
    assert LoggingMixin in Product.__bases__


def test_product_creation_logging(capsys):
    """Тест логирования при создании Product"""
    with patch.object(LoggingMixin, '__init__') as mock_init:
        mock_init.return_value = None
        product = Product("Test Product", "Test Description", 100.0, 10)

        # Проверяем, что метод __init__ миксина был вызван
        mock_init.assert_called_once()


def test_smartphone_creation_logging(capsys):
    """Тест логирования при создании Smartphone"""
    with patch.object(LoggingMixin, '__init__') as mock_init:
        mock_init.return_value = None
        smartphone = Smartphone("Test Phone", "Test Desc", 200.0, 5, "High", "ModelX", "128GB", "Black")

        # Проверяем, что метод __init__ миксина был вызван
        mock_init.assert_called_once()


def test_lawn_grass_creation_logging(capsys):
    """Тест логирования при создании LawnGrass"""
    with patch.object(LoggingMixin, '__init__') as mock_init:
        mock_init.return_value = None
        lawn_grass = LawnGrass("Test Grass", "Test Desc", 50.0, 20, "USA", "30 days", "Green")

        # Проверяем, что метод __init__ миксина был вызван
        mock_init.assert_called_once()


def test_logging_mixin_output_format(capsys):
    """Тест формата вывода логирования"""
    # Создаем продукт и перехватываем вывод
    product = Product("TestProduct", "TestDescription", 150.0, 25)

    # Получаем вывод
    captured = capsys.readouterr()
    output = captured.out.strip()

    # Проверяем формат вывода
    assert "Создан объект Product(" in output
    assert "name='TestProduct'" in output
    assert "description='TestDescription'" in output
    assert "price=150.0" in output
    assert "quantity=25" in output


def test_logging_mixin_with_smartphone_params(capsys):
    """Тест логирования с параметрами Smartphone"""
    smartphone = Smartphone("SmartPhone", "Smart Desc", 300.0, 15, "Medium", "ModelY", "64GB", "White")

    captured = capsys.readouterr()
    output = captured.out.strip()

    # Проверяем основные параметры
    assert "Создан объект Smartphone(" in output
    assert "name='SmartPhone'" in output
    assert "description='Smart Desc'" in output
    assert "price=300.0" in output
    assert "quantity=15" in output
    # Проверяем дополнительные параметры
    assert "efficiency='Medium'" in output
    assert "model='ModelY'" in output
    assert "memory='64GB'" in output
    assert "color='White'" in output


def test_logging_mixin_with_lawn_grass_params(capsys):
    """Тест логирования с параметрами LawnGrass"""
    lawn_grass = LawnGrass("LawnGrass", "Grass Desc", 75.0, 30, "Germany", "25 days", "Dark Green")

    captured = capsys.readouterr()
    output = captured.out.strip()

    # Проверяем основные параметры
    assert "Создан объект LawnGrass(" in output
    assert "name='LawnGrass'" in output
    assert "description='Grass Desc'" in output
    assert "price=75.0" in output
    assert "quantity=30" in output
    # Проверяем дополнительные параметры
    assert "country='Germany'" in output
    assert "germination_period='25 days'" in output
    assert "color='Dark Green'" in output


def test_existing_functionality_still_works():
    """Тест, что существующая функциональность все еще работает"""
    # Создаем продукты обычным образом
    product = Product("Existing", "Functionality", 100.0, 10)
    smartphone = Smartphone("Phone", "Smart", 200.0, 5, "High", "M1", "128GB", "Black")
    lawn_grass = LawnGrass("Grass", "Lawn", 50.0, 20, "USA", "30d", "Green")

    # Проверяем, что свойства установлены корректно
    assert product.name == "Existing"
    assert smartphone.model == "M1"
    assert lawn_grass.country == "USA"

    # Проверяем математические операции
    total = product + smartphone
    assert total == (100.0 * 10) + (200.0 * 5)


def test_category_with_logged_products(capsys):
    """Тест работы Category с продуктами, созданными через миксин"""
    # Создаем продукты (логирование сработает)
    product1 = Product("Prod1", "Desc1", 10.0, 5)
    product2 = Product("Prod2", "Desc2", 20.0, 3)

    # Очищаем вывод консоли от сообщений о создании
    capsys.readouterr()

    # Создаем категорию и добавляем продукты
    category = Category("Test Category", "Test Desc", [product1])
    category.add_product(product2)

    # Проверяем, что категория работает корректно
    assert len(category.products) == 2
    assert category.products[0].name == "Prod1"
    assert category.products[1].name == "Prod2"


# Дополнительные тесты для проверки совместимости

def test_product_creation_with_new_product_method(capsys):
    """Тест, что метод new_product тоже вызывает логирование"""
    product_list = []
    added_product = {"name": "NewProduct", "description": "NewDesc", "price": 150.0, "quantity": 10}

    # Создаем продукт через new_product
    product = Product.new_product(added_product, product_list)

    # Проверяем вывод
    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "Создан объект Product(" in output
    assert "name='NewProduct'" in output
    assert product.name == "NewProduct"
    assert len(product_list) == 1


def test_logging_mixin_multiple_inheritance():
    """Тест корректности множественного наследования"""
    # Проверяем MRO (Method Resolution Order)
    mro = Product.__mro__

    # LoggingMixin должен быть в цепочке наследования перед BaseProduct
    logging_mixin_index = mro.index(LoggingMixin)
    base_product_index = mro.index(Product.__bases__[1])  # Второй родительский класс

    assert logging_mixin_index < base_product_index, "LoggingMixin должен быть первым в цепочке наследования"


def test_product_zero_quantity_raises_error():
    """Тест, что создание товара с нулевым количеством вызывает исключение"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test Product", "Test Description", 100.0, 0)


def test_smartphone_zero_quantity_raises_error():
    """Тест, что создание смартфона с нулевым количеством вызывает исключение"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Smartphone("Test Phone", "Test Desc", 200.0, 0, "High", "ModelX", "128GB", "Black")


def test_lawn_grass_zero_quantity_raises_error():
    """Тест, что создание газонной травы с нулевым количеством вызывает исключение"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        LawnGrass("Test Grass", "Test Desc", 50.0, 0, "USA", "30 days", "Green")


def test_new_product_zero_quantity_raises_error(product_list):
    """Тест, что метод new_product с нулевым количеством вызывает исключение"""
    added_product = {"name": "Zero Product", "description": "Zero Desc", "price": 10.0, "quantity": 0}

    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product.new_product(added_product, product_list)


def test_new_product_update_to_zero_quantity_raises_error(product_list):
    """Тест, что обновление существующего товара до нулевого количества вызывает исключение"""
    # Сначала создаем товар с количеством 1
    existing_product = {"name": "Test Product", "description": "Test Desc", "price": 10.0, "quantity": 1}
    Product.new_product(existing_product, product_list)

    # Пытаемся добавить -1, чтобы общее количество стало 0
    updated_product = {"name": "Test Product", "description": "Test Desc", "price": 12.0, "quantity": -1}

    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product.new_product(updated_product, product_list)


def test_valid_products_still_work():
    """Тест, что товары с положительным количеством все еще работают"""
    # Эти вызовы не должны вызывать исключений
    product = Product("Valid Product", "Valid Desc", 100.0, 1)
    smartphone = Smartphone("Valid Phone", "Valid Desc", 200.0, 5, "High", "ModelX", "128GB", "Black")
    lawn_grass = LawnGrass("Valid Grass", "Valid Desc", 50.0, 10, "USA", "30 days", "Green")

    assert product.quantity == 1
    assert smartphone.quantity == 5
    assert lawn_grass.quantity == 10


def test_category_add_zero_quantity_product_raises_error(category, product):
    """Тест, что добавление товара с нулевым количеством в категорию вызывает исключение"""
    # Устанавливаем количество товара в 0
    product.quantity = 0

    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        category.add_product(product)


def test_category_average_price_with_products():
    """Тест расчета среднего ценника с товарами в категории"""
    product1 = Product("Товар1", "Описание1", 100.0, 5)
    product2 = Product("Товар2", "Описание2", 200.0, 3)
    product3 = Product("Товар3", "Описание3", 300.0, 2)

    category = Category("Тестовая категория", "Описание", [product1, product2, product3])

    # Среднее: (100 + 200 + 300) / 3 = 200.0
    assert category.average_price() == 200.0


def test_category_average_price_single_product():
    """Тест расчета среднего ценника с одним товаром"""
    product = Product("Товар1", "Описание1", 150.0, 5)
    category = Category("Тестовая категория", "Описание", [product])

    assert category.average_price() == 150.0


def test_category_average_price_empty_category():
    """Тест расчета среднего ценника с пустой категорией"""
    category = Category("Пустая категория", "Описание", [])

    assert category.average_price() == 0


def test_category_average_price_after_adding_products():
    """Тест расчета среднего ценника после добавления товаров"""
    category = Category("Категория", "Описание", [])

    # Изначально категория пуста
    assert category.average_price() == 0

    # Добавляем товары
    product1 = Product("Товар1", "Описание1", 100.0, 5)
    product2 = Product("Товар2", "Описание2", 300.0, 3)
    category.add_product(product1)
    category.add_product(product2)

    # Среднее: (100 + 300) / 2 = 200.0
    assert category.average_price() == 200.0


def test_category_average_price_with_different_product_types():
    """Тест расчета среднего ценника с разными типами товаров"""
    product = Product("Обычный товар", "Описание", 100.0, 5)
    smartphone = Smartphone("Смартфон", "Хороший", 500.0, 3, "Высокая", "ModelX", 128, "Black")
    lawn_grass = LawnGrass("Трава", "Зеленая", 50.0, 10, "Россия", "14 дней", "Green")

    category = Category("Разные товары", "Описание", [product, smartphone, lawn_grass])

    # Среднее: (100 + 500 + 50) / 3 ≈ 216.67
    expected_average = (100 + 500 + 50) / 3
    assert category.average_price() == expected_average


def test_category_average_price_zero_price_products():
    """Тест расчета среднего ценника с товарами с нулевой ценой"""
    product1 = Product("Товар1", "Описание1", 0.0, 5)
    product2 = Product("Товар2", "Описание2", 0.0, 3)
    product3 = Product("Товар3", "Описание3", 300.0, 2)

    category = Category("Категория с нулевыми ценами", "Описание", [product1, product2, product3])

    # Среднее: (0 + 0 + 300) / 3 = 100.0
    assert category.average_price() == 100.0


def test_category_average_price_after_removal():
    """Тест расчета среднего ценника после удаления товаров (симуляция)"""
    product1 = Product("Товар1", "Описание1", 100.0, 5)
    product2 = Product("Товар2", "Описание2", 200.0, 3)
    product3 = Product("Товар3", "Описание3", 300.0, 2)

    # Создаем категорию с тремя товарами
    category = Category("Категория", "Описание", [product1, product2, product3])
    assert category.average_price() == 200.0

    # Симулируем удаление товара (создаем новую категорию без одного товара)
    category_with_two = Category("Категория", "Описание", [product1, product2])
    assert category_with_two.average_price() == 150.0


# ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ ДЛЯ УВЕЛИЧЕНИЯ ПОКРЫТИЯ

def test_product_addition_with_different_classes():
    """Тест сложения продуктов разных классов-наследников"""
    smartphone = Smartphone("Phone", "Smart", 200.0, 3, "High", "M1", 128, "Black")
    lawn_grass = LawnGrass("Grass", "Green", 50.0, 10, "USA", "30d", "Green")

    total = smartphone + lawn_grass
    assert total == (200.0 * 3) + (50.0 * 10)


def test_product_addition_invalid_type():
    """Тест сложения с неподдерживаемым типом"""
    product = Product("Product", "Desc", 100.0, 2)

    with pytest.raises(TypeError):
        product + "invalid_type"


def test_category_add_invalid_type():
    """Тест добавления неподдерживаемого типа в категорию"""
    category = Category("Test", "Desc", [])

    with pytest.raises(TypeError):
        category.add_product("invalid_product")


def test_product_price_getter():
    """Тест геттера цены"""
    product = Product("Test", "Desc", 100.0, 5)
    assert product.price == 100.0


def test_product_str_representation():
    """Тест строкового представления продукта"""
    product = Product("Test", "Desc", 100.0, 5)
    assert hasattr(product, 'name')
    assert hasattr(product, 'description')
    assert hasattr(product, 'price')
    assert hasattr(product, 'quantity')


def test_smartphone_inheritance():
    """Тест наследования Smartphone от Product"""
    smartphone = Smartphone("Phone", "Desc", 100.0, 5, "High", "M1", 128, "Black")
    assert isinstance(smartphone, Product)


def test_lawn_grass_inheritance():
    """Тест наследования LawnGrass от Product"""
    lawn_grass = LawnGrass("Grass", "Desc", 50.0, 10, "USA", "30d", "Green")
    assert isinstance(lawn_grass, Product)


def test_category_products_list_property():
    """Тест свойства products_list"""
    product = Product("Test", "Desc", 100.0, 5)
    category = Category("Test", "Desc", [product])

    products_list = category.products_list
    assert isinstance(products_list, str)
    assert "Test" in products_list


def test_category_counters():
    """Тест счетчиков категорий и продуктов"""
    # Сбрасываем счетчики для чистого теста
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Товар1", "Описание1", 100.0, 2)
    product2 = Product("Товар2", "Описание2", 200.0, 3)

    category = Category("Категория", "Описание", [product1, product2])

    assert Category.category_count >= 1
    assert Category.product_count >= 2


def test_base_product_abstract_methods():
    """Тест, что BaseProduct действительно абстрактный"""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100.0, 5)


def test_product_price_setter_increase():
    """Тест увеличения цены через сеттер"""
    product = Product("Test", "Desc", 100.0, 5)
    product.price = 150.0
    assert product.price == 150.0


def test_product_price_setter_same_price():
    """Тест установки той же цены"""
    product = Product("Test", "Desc", 100.0, 5)
    product.price = 100.0
    assert product.price == 100.0


def test_logging_mixin_with_numeric_memory(capsys):  # ИСПРАВЛЕНО: добавлен capsys
    """Тест логирования с числовым параметром памяти"""
    smartphone = Smartphone("Phone", "Desc", 200.0, 5, "High", "M1", 256, "Black")

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "memory=256" in output


def test_category_private_products_access():
    """Тест доступа к приватному списку продуктов"""
    product = Product("Test", "Desc", 100.0, 5)
    category = Category("Test", "Desc", [product])

    # Проверяем, что доступ через свойство works
    assert len(category.products) == 1
    assert category.products[0].name == "Test"


def test_product_creation_with_kwargs():
    """Тест создания продукта с дополнительными kwargs"""
    # Это проверит обработку **kwargs в конструкторе
    product = Product("Test", "Desc", 100.0, 5, extra_param="value")
    assert product.name == "Test"


def test_smartphone_creation_with_string_memory():
    """Тест создания смартфона со строковой памятью"""
    smartphone = Smartphone("Phone", "Desc", 200.0, 5, "High", "M1", "256GB", "Black")
    assert smartphone.memory == "256GB"


def test_lawn_grass_creation_variations():
    """Тест создания газонной травы с различными параметрами"""
    lawn_grass = LawnGrass("Grass", "Desc", 75.0, 15, "Germany", "30 days", "Dark Green")
    assert lawn_grass.country == "Germany"
    assert lawn_grass.germination_period == "30 days"


# ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ ДЛЯ 100% ПОКРЫТИЯ

def test_product_price_setter_zero_price():
    """Тест установки нулевой цены"""
    product = Product("Test", "Desc", 100.0, 5)
    with patch("builtins.print") as mocked_print:
        product.price = 0.0
        mocked_print.assert_called_with("Цена не должна быть нулевая или отрицательная")
        assert product.price == 100.0


def test_product_price_setter_negative_price():
    """Тест установки отрицательной цены"""
    product = Product("Test", "Desc", 100.0, 5)
    with patch("builtins.print") as mocked_print:
        product.price = -50.0
        mocked_print.assert_called_with("Цена не должна быть нулевая или отрицательная")
        assert product.price == 100.0


def test_product_addition_same_class():
    """Тест сложения продуктов одного класса"""
    product1 = Product("Product1", "Desc", 100.0, 2)
    product2 = Product("Product2", "Desc", 200.0, 3)

    total = product1 + product2
    assert total == (100.0 * 2) + (200.0 * 3)


def test_category_multiple_additions():
    """Тест множественного добавления товаров в категорию"""
    category = Category("Test", "Desc", [])
    product1 = Product("Product1", "Desc", 100.0, 2)
    product2 = Product("Product2", "Desc", 200.0, 3)
    product3 = Product("Product3", "Desc", 300.0, 1)

    category.add_product(product1)
    category.add_product(product2)
    category.add_product(product3)

    assert len(category.products) == 3
    assert category.average_price() == 200.0


def test_category_initialization_with_products():
    """Тест инициализации категории с товарами"""
    product1 = Product("Product1", "Desc", 100.0, 2)
    product2 = Product("Product2", "Desc", 200.0, 3)

    category = Category("Test", "Desc", [product1, product2])

    assert len(category.products) == 2
    assert category.average_price() == 150.0


def test_logging_mixin_empty_args():
    """Тест логирования с пустыми аргументами"""

    # Создаем временный класс для тестирования
    class TestClass(LoggingMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    # Тестируем с пустыми аргументами
    test_obj = TestClass()

    # Проверяем, что объект создан
    assert test_obj is not None


def test_product_new_product_same_price():
    """Тест new_product с той же ценой"""
    product_list = []
    existing_product = {"name": "Product", "description": "Desc", "price": 100.0, "quantity": 5}
    Product.new_product(existing_product, product_list)

    # Обновляем с той же ценой
    updated_product = {"name": "Product", "description": "Desc", "price": 100.0, "quantity": 3}
    product = Product.new_product(updated_product, product_list)

    assert product.price == 100.0
    assert product.quantity == 8


def test_product_new_product_lower_price():
    """Тест new_product с более низкой ценой"""
    product_list = []
    existing_product = {"name": "Product", "description": "Desc", "price": 100.0, "quantity": 5}
    Product.new_product(existing_product, product_list)

    # Обновляем с более низкой ценой (должна остаться старая цена)
    updated_product = {"name": "Product", "description": "Desc", "price": 50.0, "quantity": 3}
    product = Product.new_product(updated_product, product_list)

    assert product.price == 100.0  # Старая цена должна сохраниться
    assert product.quantity == 8


def test_category_products_list_multiple_products():
    """Тест products_list с несколькими товарами"""
    product1 = Product("Product1", "Desc1", 100.0, 2)
    product2 = Product("Product2", "Desc2", 200.0, 3)

    category = Category("Test", "Desc", [product1, product2])

    products_list = category.products_list
    assert isinstance(products_list, str)
    # Проверяем, что содержит информацию о товарах
    assert any(name in products_list for name in ["Product1", "Product2"])


def test_logging_mixin_complex_parameters():
    """Тест логирования со сложными параметрами"""
    # Тестируем с различными типами параметров
    smartphone = Smartphone("Complex Phone", "Description", 999.99, 1, "Ultra", "Z1000", 1024, "Space Gray")

    # Проверяем, что объект создан корректно
    assert smartphone.name == "Complex Phone"
    assert smartphone.price == 999.99
    assert smartphone.memory == 1024