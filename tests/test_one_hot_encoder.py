"""Тесты для модуля one_hot_encoder"""
import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    """Тесты для метода fit_transform"""

    def test_transform_list(self):
        """Тест для проверки корректности работы со списком"""
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_transform_dict(self):
        """Тест для проверки корректности работы со словарем"""
        sizes = {'S': 'small', 'M': 'medium', 'L': 'large'}
        transformed_sizes = fit_transform(sizes)
        transformed_keys = [x[0] for x in transformed_sizes]
        for key in sizes:
            self.assertIn(key, transformed_keys)

    def test_transform_str(self):
        """Тест для проверки корректности работы со строкой"""
        sizes = list('SMLSMLSS')
        transformed_sizes = fit_transform(sizes)
        sum_ones = sum(sum(x[1]) for x in transformed_sizes)
        self.assertEqual(len(sizes), sum_ones)

    def test_no_arguments(self):
        """Тест для проверки наличия ошибки при отсутствии параметров"""
        with self.assertRaises(TypeError):
            fit_transform()

    def test_type_error(self):
        """Тест для проверки наличия ошибки при параметре неверного типа"""
        with self.assertRaises(TypeError):
            fit_transform(345)
