"""Тесты для модуля one_hot_encoder"""
import pytest
from one_hot_encoder import fit_transform


@pytest.fixture
def cities():
    """
    Пример работы с фикстурой для случая, когда одни данные нужно
    использовать в нескольких тестах
    """
    return ['Moscow', 'New York', 'Moscow', 'London']


@pytest.fixture
def exp_transformed_cities():
    """Пример работы с фикстурой. В этой фикстуре нет необходимости"""
    return [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]


def test_transform_list(cities, exp_transformed_cities):
    """Тест для проверки корректности работы со списком"""
    transformed_cities = fit_transform(cities)
    assert transformed_cities == exp_transformed_cities


def test_transform_dict():
    """Тест для проверки корректности работы со словарем"""
    sizes = {'S': 'small', 'M': 'medium', 'L': 'large'}
    transformed_sizes = fit_transform(sizes)
    transformed_keys = [x[0] for x in transformed_sizes]
    for key in sizes:
        assert key in transformed_keys


def test_transform_sum(cities):
    """Тест для проверки количества единиц в результате"""
    transformed_cities = fit_transform(cities)
    sum_ones = sum(sum(x[1]) for x in transformed_cities)
    assert len(cities) == sum_ones


@pytest.mark.parametrize(
    "insert_value", [*[], 345, True, None]
)
def test_no_arguments(insert_value):
    """Тест для проверки наличия ошибки при неверных параметрах"""
    with pytest.raises(TypeError):
        fit_transform(insert_value)
