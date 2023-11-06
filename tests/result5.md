## Тестирование `what_is_year_now` с использованием `unittest`

```powershell
py -m unittest -v test_what_is_year_now
test_accept_wrong_year (test_what_is_year_now.TestWhatIsYearNow)
Тест для проверки отсутствия ошибки при передаче будущего года ... ok
test_dates_with_dash (test_what_is_year_now.TestWhatIsYearNow)
Тест для проверки работы с датами формата 2019-03-01 ... ok
test_dates_with_dot (test_what_is_year_now.TestWhatIsYearNow)
Тест для проверки работы с датами формата 01.03.2019 ... ok
test_wrong_date (test_what_is_year_now.TestWhatIsYearNow)
Тест для проверки наличия ошибки при некорректном формате даты ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.004s

OK
```