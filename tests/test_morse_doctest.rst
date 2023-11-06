Тесты doctest для модуля morse

>>> from morse import decode, encode

>>> encode('SOS')
'... --- ...'

>>> encode('PYTHON')
'.--. -.-- - .... --- -.'

>>> encode(345)
Traceback (most recent call last):
    ...
TypeError: 'int' object is not iterable

>>> decode('... --- ...')
'SOS'

>>> decode('.--. -.-- - .... --- -.')
'PYTHON'

>>> decode(345)  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
AttributeError: ...
