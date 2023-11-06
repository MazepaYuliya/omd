## Тестирование `fit_transform` с использованием `unittest`

```powershell
PS C:\Users\lm137\Desktop\Education\omd\tests> py -m unittest -v test_one_hot_encoder
test_no_arguments (test_one_hot_encoder.TestFitTransform)
Тест для проверки наличия ошибки при отсутствии параметров ... ok
test_transform_dict (test_one_hot_encoder.TestFitTransform)
Тест для проверки корректности работы со словарем ... ['S', 'M', 'L']
{'M', 'L', 'S'}
ok
test_transform_list (test_one_hot_encoder.TestFitTransform)
Тест для проверки корректности работы со списком ... ['Moscow', 'New York', 'Moscow', 'London']
{'London', 'Moscow', 'New York'}
ok
test_transform_str (test_one_hot_encoder.TestFitTransform)
Тест для проверки корректности работы со строкой ... ['S', 'M', 'L', 'S', 'M', 'L', 'S', 'S']
{'M', 'L', 'S'}
ok
test_type_error (test_one_hot_encoder.TestFitTransform)
Тест для проверки наличия ошибки при параметре неверного типа ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.008s

OK
```