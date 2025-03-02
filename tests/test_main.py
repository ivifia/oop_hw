import pytest
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
