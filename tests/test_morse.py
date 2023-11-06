"""Тесты для модуля morse"""
from morse import decode, encode
import pytest


@pytest.mark.parametrize(
    'source_string, result',
    [
        (encode('SOS'), '... --- ...'),
        (encode('PYTHON'), '.--. -.-- - .... --- -.'),
        (encode('NOV/2023'), '-. --- ...- -..-. ..--- ----- ..--- ...--'),
    ]
)
def test_encode(source_string, result):
    """Тесты для метода encode при корректной работе"""
    assert source_string == result


@pytest.mark.parametrize(
    'input_value', [345, True]
)
def test_encode_type_error(input_value):
    """Тесты для метода encode при параметрах с неверным типом"""
    with pytest.raises(TypeError):
        encode(input_value)


@pytest.mark.parametrize(
    'input_value', ['sos', 'nov 2023', ['SOS']]
)
def test_encode_key_error(input_value):
    """
    Тесты для метода encode для строки, кодирование которой не предусмотрено
    """
    with pytest.raises(KeyError):
        encode(input_value)


@pytest.mark.parametrize(
    'source_string, result',
    [
        (decode('... --- ...'), 'SOS'),
        (decode('.--. -.-- - ....          --- -.'), 'PYTHON'),
        (decode('-. --- ...- -..-. ..--- ----- ..--- ...--'), 'NOV/2023'),
    ]
)
def test_decode(source_string, result):
    """Тесты для метода decode при корректной работе"""
    assert source_string == result


@pytest.mark.parametrize(
    'input_value', [345, True, ['SOS']]
)
def test_decode_type_error(input_value):
    """Тесты для метода decode при параметрах с неверным типом"""
    with pytest.raises(AttributeError):
        decode(input_value)


@pytest.mark.parametrize(
    'input_value', ['sos', 'nov 2023', '........']
)
def test_decode_key_error(input_value):
    """
    Тесты для метода decode для строки, декодирование которой не предусмотрено
    """
    with pytest.raises(KeyError):
        decode(input_value)
