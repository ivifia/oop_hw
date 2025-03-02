import pytest
from unittest.mock import patch
from src.main import Product, Category

@pytest.fixture()
def test_Category():
    return Category("Иван", "lflflf", ["banana", 3, "pop"], )


def test_init_category(test_Category):
    assert test_Category.name == "Иван"
    assert test_Category.description == "lflflf"
    assert test_Category.products == ["banana", 3, "pop"]
    assert test_Category.category_count == 1
    assert test_Category.product_count == 3


@pytest.fixture()
def test_Product():
    return Product("Иван", "lal", 12.0, 4)


def test_init_product(test_Product):
    assert test_Product.name == "Иван"
    assert test_Product.description == "lal"
    assert test_Product.price == 12.0
    assert test_Product.quantity == 4
def test_set_price(test_Product):
    test_Product.check_price = 15.0
    assert test_Product.check_price == 15.0
def test_set_price_invalid(test_Product):
    with patch("builtins.print") as mocked_print:
        test_Product.check_price = -5.0
        mocked_print.assert_called_with("Цена не должна быть нулевая или отрицательная")
        assert test_Product.check_price == 12.0
def test_set_price_decrease_confirmation(test_Product):
    with patch("builtins.input", return_value="y"):
        test_Product.check_price = 10.0
        assert test_Product.check_price == 10.0

    with patch("builtins.input", return_value="n"):
        test_Product.check_price = 8.0
        assert test_Product.check_price == 10.0
@pytest.fixture()
def product_list():
    return []


def test_new_product_addition(product_list):
    added_product = {"name": "Яблоко", "description": "Зеленое", "price": 10.0, "quantity": 5}
    product = Product.new_product(added_product, product_list)

    assert len(product_list) == 1
    assert product.name == "Яблоко"
    assert product.check_price == 10.0
    assert product.quantity == 5



def test_new_product_update_existing(product_list):
    existing_product = {"name": "Яблоко", "description": "Зеленое", "price": 10.0, "quantity": 5}
    Product.new_product(existing_product, product_list)

    updated_product = {"name": "Яблоко", "description": "Красное", "price": 12.0, "quantity": 3}
    product = Product.new_product(updated_product, product_list)

    assert len(product_list) == 1
    assert product.name == "Яблоко"
    assert product.check_price == 12.0
    assert product.quantity == 8