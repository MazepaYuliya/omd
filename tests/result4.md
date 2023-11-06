## Тестирование `fit_transform` с использованием `pytest`

```powershell
PS C:\Users\lm137\Desktop\Education\omd> py -m pytest -v .\tests\test_one_hot_encoder_pytest.py
========================================== test session starts =============================================
platform win32 -- Python 3.9.10, pytest-7.4.3, pluggy-1.3.0 -- C:\Users\lm137\AppData\Local\Programs\Python\Python39\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lm137\Desktop\Education\omd
plugins: anyio-3.7.1, dash-2.7.1, typeguard-2.13.3
collected 6 items

tests/test_one_hot_encoder_pytest.py::test_transform_list PASSED                                      [ 16%]
tests/test_one_hot_encoder_pytest.py::test_transform_dict PASSED                                      [ 33%]
tests/test_one_hot_encoder_pytest.py::test_transform_sum PASSED                                       [ 50%]
tests/test_one_hot_encoder_pytest.py::test_no_arguments[345] PASSED                                   [ 66%]
tests/test_one_hot_encoder_pytest.py::test_no_arguments[True] PASSED                                  [ 83%]
tests/test_one_hot_encoder_pytest.py::test_no_arguments[None] PASSED                                  [100%]

=========================================== 6 passed in 0.10s ==============================================
```