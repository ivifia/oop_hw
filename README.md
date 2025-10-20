#Код для обработки категорий и товаров. 
#Обработка находится в файле src/main.py, тесты в tests/test_main.py
#добавлена функция сложения в разделе Products, а так же классы smartphone и Lawngrass
. Расширен функционал добавления продуктов в категорию
# покрытие тестов:
collecting ... collected 65 items

test_main.py::test_init_category Создан объект Product(name='banana', description='yellow fruit', price=10.0, quantity=5)
Создан объект Product(name='pop', description='drink', price=20.0, quantity=3)
PASSED                                  [  1%]
test_main.py::test_init_product Создан объект Product(name='Иван', description='lal', price=12.0, quantity=4)
PASSED                                   [  3%]
test_main.py::test_set_price Создан объект Product(name='Иван', description='lal', price=12.0, quantity=4)
PASSED                                      [  4%]
test_main.py::test_set_price_invalid Создан объект Product(name='Иван', description='lal', price=12.0, quantity=4)
PASSED                              [  6%]
test_main.py::test_set_price_decrease_confirmation Создан объект Product(name='Иван', description='lal', price=12.0, quantity=4)
PASSED                [  7%]Цена обновлена на 10.0
Изменение цены отменено.

test_main.py::test_new_product_addition PASSED                           [  9%]Создан объект Product(name='Яблоко', description='Зеленое', price=10.0, quantity=5)

test_main.py::test_new_product_update_existing PASSED                    [ 10%]Создан объект Product(name='Яблоко', description='Зеленое', price=10.0, quantity=5)

test_main.py::test_init_smartphone Создан объект Smartphone(name='Samsung A73', description='good smartphone', price=50.0, quantity=35, efficiency='high', model='A73', memory=128, color='grey')
PASSED                                [ 12%]
test_main.py::test_init_LawnGrass Создан объект LawnGrass(name='Grass_cuter', description='best', price=50.0, quantity=35, country='Germany', germination_period='73 days', color='grey')
PASSED                                 [ 13%]
test_main.py::test_product_add Создан объект Product(name='Телефон', description='Смартфон', price=50000, quantity=3)
Создан объект Product(name='Ноутбук', description='Игровой', price=100000, quantity=2)
PASSED                                    [ 15%]
test_main.py::test_add_valid_product Создан объект Product(name='Телефон', description='Смартфон', price=50000, quantity=3)
PASSED                              [ 16%]
test_main.py::test_add_smartphone Создан объект Smartphone(name='iPhone', description='Премиум', price=100000, quantity=5, efficiency='A15', model='13 Pro', memory=256, color='Silver')
PASSED                                 [ 18%]
test_main.py::test_add_lawn_grass Создан объект LawnGrass(name='Трава', description='Для газона', price=500, quantity=10, country='Россия', germination_period='14 дней', color='Зеленая')
PASSED                                 [ 20%]
test_main.py::test_logging_mixin_inheritance PASSED                      [ 21%]
test_main.py::test_product_creation_logging PASSED                       [ 23%]
test_main.py::test_smartphone_creation_logging PASSED                    [ 24%]
test_main.py::test_lawn_grass_creation_logging PASSED                    [ 26%]
test_main.py::test_logging_mixin_output_format PASSED                    [ 27%]
test_main.py::test_logging_mixin_with_smartphone_params PASSED           [ 29%]
test_main.py::test_logging_mixin_with_lawn_grass_params PASSED           [ 30%]
test_main.py::test_existing_functionality_still_works PASSED             [ 32%]Создан объект Product(name='Existing', description='Functionality', price=100.0, quantity=10)
Создан объект Smartphone(name='Phone', description='Smart', price=200.0, quantity=5, efficiency='High', model='M1', memory='128GB', color='Black')
Создан объект LawnGrass(name='Grass', description='Lawn', price=50.0, quantity=20, country='USA', germination_period='30d', color='Green')

test_main.py::test_category_with_logged_products PASSED                  [ 33%]
test_main.py::test_product_creation_with_new_product_method PASSED       [ 35%]
test_main.py::test_logging_mixin_multiple_inheritance PASSED             [ 36%]
test_main.py::test_product_zero_quantity_raises_error PASSED             [ 38%]
test_main.py::test_smartphone_zero_quantity_raises_error PASSED          [ 40%]
test_main.py::test_lawn_grass_zero_quantity_raises_error PASSED          [ 41%]
test_main.py::test_new_product_zero_quantity_raises_error PASSED         [ 43%]
test_main.py::test_new_product_update_to_zero_quantity_raises_error PASSED [ 44%]Создан объект Product(name='Test Product', description='Test Desc', price=10.0, quantity=1)

test_main.py::test_valid_products_still_work PASSED                      [ 46%]Создан объект Product(name='Valid Product', description='Valid Desc', price=100.0, quantity=1)
Создан объект Smartphone(name='Valid Phone', description='Valid Desc', price=200.0, quantity=5, efficiency='High', model='ModelX', memory='128GB', color='Black')
Создан объект LawnGrass(name='Valid Grass', description='Valid Desc', price=50.0, quantity=10, country='USA', germination_period='30 days', color='Green')

test_main.py::test_category_add_zero_quantity_product_raises_error Создан объект Product(name='Телефон', description='Смартфон', price=50000, quantity=3)
PASSED [ 47%]
test_main.py::test_category_average_price_with_products PASSED           [ 49%]Создан объект Product(name='Товар1', description='Описание1', price=100.0, quantity=5)
Создан объект Product(name='Товар2', description='Описание2', price=200.0, quantity=3)
Создан объект Product(name='Товар3', description='Описание3', price=300.0, quantity=2)

test_main.py::test_category_average_price_single_product PASSED          [ 50%]Создан объект Product(name='Товар1', description='Описание1', price=150.0, quantity=5)

test_main.py::test_category_average_price_empty_category PASSED          [ 52%]
test_main.py::test_category_average_price_after_adding_products PASSED   [ 53%]Создан объект Product(name='Товар1', description='Описание1', price=100.0, quantity=5)
Создан объект Product(name='Товар2', description='Описание2', price=300.0, quantity=3)

test_main.py::test_category_average_price_with_different_product_types PASSED [ 55%]Создан объект Product(name='Обычный товар', description='Описание', price=100.0, quantity=5)
Создан объект Smartphone(name='Смартфон', description='Хороший', price=500.0, quantity=3, efficiency='Высокая', model='ModelX', memory=128, color='Black')
Создан объект LawnGrass(name='Трава', description='Зеленая', price=50.0, quantity=10, country='Россия', germination_period='14 дней', color='Green')

test_main.py::test_category_average_price_zero_price_products PASSED     [ 56%]Создан объект Product(name='Товар1', description='Описание1', price=0.0, quantity=5)
Создан объект Product(name='Товар2', description='Описание2', price=0.0, quantity=3)
Создан объект Product(name='Товар3', description='Описание3', price=300.0, quantity=2)

test_main.py::test_category_average_price_after_removal PASSED           [ 58%]Создан объект Product(name='Товар1', description='Описание1', price=100.0, quantity=5)
Создан объект Product(name='Товар2', description='Описание2', price=200.0, quantity=3)
Создан объект Product(name='Товар3', description='Описание3', price=300.0, quantity=2)

test_main.py::test_product_addition_with_different_classes PASSED        [ 60%]Создан объект Smartphone(name='Phone', description='Smart', price=200.0, quantity=3, efficiency='High', model='M1', memory=128, color='Black')
Создан объект LawnGrass(name='Grass', description='Green', price=50.0, quantity=10, country='USA', germination_period='30d', color='Green')

test_main.py::test_product_addition_invalid_type PASSED                  [ 61%]Создан объект Product(name='Product', description='Desc', price=100.0, quantity=2)

test_main.py::test_category_add_invalid_type PASSED                      [ 63%]
test_main.py::test_product_price_getter PASSED                           [ 64%]Создан объект Product(name='Test', description='Desc', price=100.0, quantity=5)

test_main.py::test_product_str_representation PASSED                     [ 66%]Создан объект Product(name='Test', description='Desc', price=100.0, quantity=5)

test_main.py::test_smartphone_inheritance PASSED                         [ 67%]Создан объект Smartphone(name='Phone', description='Desc', price=100.0, quantity=5, efficiency='High', model='M1', memory=128, color='Black')

test_main.py::test_lawn_grass_inheritance PASSED                         [ 69%]Создан объект LawnGrass(name='Grass', description='Desc', price=50.0, quantity=10, country='USA', germination_period='30d', color='Green')

test_main.py::test_category_products_list_property PASSED                [ 70%]Создан объект Product(name='Test', description='Desc', price=100.0, quantity=5)

test_main.py::test_category_counters PASSED                              [ 72%]Создан объект Product(name='Товар1', description='Описание1', price=100.0, quantity=2)
Создан объект Product(name='Товар2', description='Описание2', price=200.0, quantity=3)

test_main.py::test_base_product_abstract_methods PASSED                  [ 73%]
test_main.py::test_product_price_setter_increase PASSED                  [ 75%]Создан объект Product(name='Test', description='Desc', price=100.0, quantity=5)

test_main.py::test_product_price_setter_same_price PASSED                [ 76%]Создан объект Product(name='Test', description='Desc', price=100.0, quantity=5)

test_main.py::test_logging_mixin_with_numeric_memory PASSED              [ 78%]
test_main.py::test_category_private_products_access PASSED               [ 80%]Создан объект Product(name='Test', description='Desc', price=100.0, quantity=5)

test_main.py::test_product_creation_with_kwargs PASSED                   [ 81%]Создан объект Product(name='Test', description='Desc', price=100.0, quantity=5, extra_param='value')

test_main.py::test_smartphone_creation_with_string_memory PASSED         [ 83%]Создан объект Smartphone(name='Phone', description='Desc', price=200.0, quantity=5, efficiency='High', model='M1', memory='256GB', color='Black')

test_main.py::test_lawn_grass_creation_variations PASSED                 [ 84%]Создан объект LawnGrass(name='Grass', description='Desc', price=75.0, quantity=15, country='Germany', germination_period='30 days', color='Dark Green')

test_main.py::test_product_price_setter_zero_price PASSED                [ 86%]Создан объект Product(name='Test', description='Desc', price=100.0, quantity=5)

test_main.py::test_product_price_setter_negative_price PASSED            [ 87%]Создан объект Product(name='Test', description='Desc', price=100.0, quantity=5)

test_main.py::test_product_addition_same_class PASSED                    [ 89%]Создан объект Product(name='Product1', description='Desc', price=100.0, quantity=2)
Создан объект Product(name='Product2', description='Desc', price=200.0, quantity=3)

test_main.py::test_category_multiple_additions PASSED                    [ 90%]Создан объект Product(name='Product1', description='Desc', price=100.0, quantity=2)
Создан объект Product(name='Product2', description='Desc', price=200.0, quantity=3)
Создан объект Product(name='Product3', description='Desc', price=300.0, quantity=1)

test_main.py::test_category_initialization_with_products PASSED          [ 92%]Создан объект Product(name='Product1', description='Desc', price=100.0, quantity=2)
Создан объект Product(name='Product2', description='Desc', price=200.0, quantity=3)

test_main.py::test_logging_mixin_empty_args PASSED                       [ 93%]Создан объект TestClass()

test_main.py::test_product_new_product_same_price PASSED                 [ 95%]Создан объект Product(name='Product', description='Desc', price=100.0, quantity=5)

test_main.py::test_product_new_product_lower_price PASSED                [ 96%]Создан объект Product(name='Product', description='Desc', price=100.0, quantity=5)

test_main.py::test_category_products_list_multiple_products PASSED       [ 98%]Создан объект Product(name='Product1', description='Desc1', price=100.0, quantity=2)
Создан объект Product(name='Product2', description='Desc2', price=200.0, quantity=3)

test_main.py::test_logging_mixin_complex_parameters PASSED               [100%]Создан объект Smartphone(name='Complex Phone', description='Description', price=999.99, quantity=1, efficiency='Ultra', model='Z1000', memory=1024, color='Space Gray')


============================= 65 passed in 0.24s ==============================

