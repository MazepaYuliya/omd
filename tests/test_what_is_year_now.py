"""Тесты для модуля what_is_year_now"""
import json
import unittest
from io import StringIO
from unittest.mock import Mock, patch
from what_is_year_now import what_is_year_now


def dump_dict(dict_to_dump):
    """Метод для получения json из словаря"""
    file_stream = StringIO()
    json.dump(dict_to_dump, file_stream)
    file_stream.seek(0)
    return file_stream


class TestWhatIsYearNow(unittest.TestCase):
    """Тесты для метода what_is_year_now"""

    @patch(
        'what_is_year_now.urllib.request.urlopen',
        Mock(return_value=dump_dict({'currentDateTime': '2019-03-01'}))
    )
    def test_dates_with_dash(self):
        """Тест для проверки работы с датами формата 2019-03-01"""
        exp_year = 2019
        year = what_is_year_now()
        self.assertEqual(year, exp_year)

    @patch(
        'what_is_year_now.urllib.request.urlopen',
        Mock(return_value=dump_dict({'currentDateTime': '01.03.2019'}))
    )
    def test_dates_with_dot(self):
        """Тест для проверки работы с датами формата 01.03.2019"""
        exp_year = 2019
        year = what_is_year_now()
        self.assertEqual(year, exp_year)

    @patch(
        'what_is_year_now.urllib.request.urlopen',
        Mock(return_value=dump_dict({'currentDateTime': '01/03/2019'}))
    )
    def test_wrong_date(self):
        """Тест для проверки наличия ошибки при некорректном формате даты"""
        with self.assertRaises(ValueError):
            what_is_year_now()

    @patch(
        'what_is_year_now.urllib.request.urlopen',
        Mock(return_value=dump_dict({'currentDateTime': '01.03.9999'}))
    )
    def test_accept_wrong_year(self):
        """Тест для проверки отсутствия ошибки при передаче будущего года"""
        exp_year = 9999
        year = what_is_year_now()
        self.assertEqual(year, exp_year)
