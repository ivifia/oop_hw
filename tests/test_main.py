import pytest
from unittest.mock import patch
from src.Products import Product,Smartphone,LawnGrass
from src.Category import Category

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
    assert test_Category.category_count >= 1  # Может быть больше, если другие тесты уже увеличивали счетчик
    assert test_Category.product_count >= 2  # Аналогично для product_count

@pytest.fixture()
def test_Product():
    return Product("Иван", "lal", 12.0, 4)

def test_init_product(test_Product):
    assert test_Product.name == "Иван"
    assert test_Product.description == "lal"
    assert test_Product.price == 12.0  # Используем price вместо check_price
    assert test_Product.quantity == 4

def test_set_price(test_Product):
    test_Product.check_price = 15.0
    assert test_Product.price == 15.0

def test_set_price_invalid(test_Product):
    with patch("builtins.print") as mocked_print:
        test_Product.check_price = -5.0
        mocked_print.assert_called_with("Цена не должна быть нулевая или отрицательная")
        assert test_Product.price == 12.0

def test_set_price_decrease_confirmation(test_Product):
    with patch("builtins.input", return_value="y"):
        test_Product.check_price = 10.0
        assert test_Product.price == 10.0

    with patch("builtins.input", return_value="n"):
        test_Product.check_price = 8.0
        assert test_Product.price == 10.0

@pytest.fixture()
def product_list():
    return []

def test_new_product_addition(product_list):
    added_product = {"name": "Яблоко", "description": "Зеленое", "price": 10.0, "quantity": 5}
    product = Product.new_product(added_product, product_list)

    assert len(product_list) == 1
    assert product.name == "Яблоко"
    assert product.price == 10.0  # Используем price вместо check_price
    assert product.quantity == 5

def test_new_product_update_existing(product_list):
    existing_product = {"name": "Яблоко", "description": "Зеленое", "price": 10.0, "quantity": 5}
    Product.new_product(existing_product, product_list)

    updated_product = {"name": "Яблоко", "description": "Красное", "price": 12.0, "quantity": 3}
    product = Product.new_product(updated_product, product_list)

    assert len(product_list) == 1
    assert product.name == "Яблоко"
    assert product.price == 12.0  # Используем price вместо check_price
    assert product.quantity == 8
@pytest.fixture()
def test_Smartphone():
    return Smartphone("Samsung A73","good smartphone",50.000,35,"high","A73",128,"grey")
def test_init_smatrphone(test_Smartphone):
    assert test_Smartphone.name=="Samsung A73"
    assert test_Smartphone.description=="good smartphone"
    assert test_Smartphone.price == 50.000
    assert test_Smartphone.quantity ==35
    assert test_Smartphone.efficiency =="high"
    assert test_Smartphone.model =="A73"
    assert test_Smartphone.memory == 128
    assert test_Smartphone.color == "grey"
@pytest.fixture()
def test_LawnGrass():
    return LawnGrass("Grass_cuter","best",50.000,35,"Germany",73,"grey",)
def test_init_LawnGrass(test_LawnGrass):
    assert test_LawnGrass.name == "Grass_cuter"
    assert test_LawnGrass.description == "best"
    assert test_LawnGrass.price == 50.000
    assert test_LawnGrass.quantity == 35
    assert test_LawnGrass.country == "Germany"
    assert test_LawnGrass.germination_period == 73
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
    return Smartphone("iPhone", "Премиум", 100000, 5, "A15", "13 Pro", "256GB", "Silver")

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



