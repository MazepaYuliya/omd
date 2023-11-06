## Тестирование функции `encode` и `decode` с использование `doctest`

```powershell
py -m doctest -o NORMALIZE_WHITESPACE -o IGNORE_EXCEPTION_DETAIL -v test_morse_doctest.rst
Trying:
    from morse import decode, encode
Expecting nothing
ok
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('PYTHON')
Expecting:
    '.--. -.-- - .... --- -.'
ok
Trying:
    encode(345)
Expecting:
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
ok
Trying:
    decode('... --- ...')
Expecting:
    'SOS'
ok
Trying:
    decode('.--. -.-- - .... --- -.')
Expecting:
    'PYTHON'
ok
Trying:
    decode(345)
Expecting:
    Traceback (most recent call last):
        ...
    AttributeError: ...
ok
1 items passed all tests:
   7 tests in test_morse_doctest.rst
7 tests in 1 items.
7 passed and 0 failed.
Test passed.
```