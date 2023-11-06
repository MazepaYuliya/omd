## Тестирование функции `encode` и `decode` с использованием параметрического теста `pytest`

```powershell
PS C:\Users\lm137\Desktop\Education\omd> py -m pytest .\tests\test_morse.py
============================================ test session starts ==========================================
platform win32 -- Python 3.9.10, pytest-7.4.3, pluggy-1.3.0
rootdir: C:\Users\lm137\Desktop\Education\omd
plugins: anyio-3.7.1, dash-2.7.1, typeguard-2.13.3
collected 17 items

tests/test_morse.py::test_encode[... --- ...-... --- ...] PASSED                                     [  5%]
tests/test_morse.py::test_encode[.--. -.-- - .... --- -.-.--. -.-- - .... --- -.] PASSED             [ 11%]
tests/test_morse.py::test_encode[-. --- ...- -..-. ..--- ----- ..--- ...----. --- ...- -..-. ..--- ----- ..--- ...--] PASSED [ 17%]
tests/test_morse.py::test_encode_type_error[345] PASSED                                              [ 23%]
tests/test_morse.py::test_encode_type_error[True] PASSED                                             [ 29%]
tests/test_morse.py::test_encode_key_error[sos] PASSED                                               [ 35%]
tests/test_morse.py::test_encode_key_error[nov 2023] PASSED                                          [ 41%]
tests/test_morse.py::test_encode_key_error[input_value2] PASSED                                      [ 47%]
tests/test_morse.py::test_decode[SOS-SOS] PASSED                                                     [ 52%]
tests/test_morse.py::test_decode[PYTHON-PYTHON] PASSED                                               [ 58%]
tests/test_morse.py::test_decode[NOV/2023-NOV/2023] PASSED                                           [ 64%]
tests/test_morse.py::test_decode_type_error[345] PASSED                                              [ 70%]
tests/test_morse.py::test_decode_type_error[True] PASSED                                             [ 76%]
tests/test_morse.py::test_decode_type_error[input_value2] PASSED                                     [ 82%]
tests/test_morse.py::test_decode_key_error[sos] PASSED                                               [ 88%]
tests/test_morse.py::test_decode_key_error[nov 2023] PASSED                                          [ 94%]
tests/test_morse.py::test_decode_key_error[........] PASSED                                          [100%]

=========================================== 17 passed in 0.20s ============================================
```