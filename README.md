# Sprint_7
API_tests
API Автотест для проекта  - сервис аренды самокатов - https://qa-scooter.praktikum-services.ru
Автотесты покрываеют регистрацию и авторизацию курьеров, создание заказа по цветам и вывод списка заказов

```
1. Создание проекта для автоматизированного тестирования сервиса
Создать в IDE новый проект
Развернуть тестовое окуржение
В корне дериктории добавить файл .gitignore - (JetBrains,Python), чтобы в проект не попало ничего лишнего
В корне дериктории создать папку tests - в ней заводить файлы с тестами в разрезе функционала
В корне дериктории создать README.md c описанием функционала и структуры проекта

```
```
2. Как добавить новый тест
- Создать новый файл теста в директории `tests` с префиксом `test_`:
test_new_feature.py
Написать класс TestSomeFeature():
Все методы начинать с префиксом `test_`
В конце каждого метода добпавлять assert
```
```
4. Импорты:
import pytest
import allure
import requests
```
```
Запустить тесты и убедиться, что все проходят успешно:
Команда для запуска всех тестов: pytest -v
Команда дляь запуска тестов c формированием отчетов: pytest -v  --alluredir=allure_results
Команда для просмотра html отчета в браузере: allure serve allure_results
# добавляем папку с отчётом Allure к файлам. Ключ -f пригодится, если папка target указана в .gitignore
git add -f .\target\allure-results\.
# выполняем коммит
git commit -m "add allure report"
# так отправишь файлы в удалённый репозиторий
git push 

# Как внести изменения
1. Создать отдельную ветку для разработки:
```
```
git checkout -b feature/new_feature
```
```
2. Внести необходимые изменения в тесты.
3. Запустить тесты и убедиться, что все проходят успешно:
```
```
4. Закоммитить изменения:
git commit -m "Add new feature"
```
```
5. Запушить изменения в репозиторий:
git push origin feature/new_feature
```
```
6. Создать Pull Request на GitHub и ожидать ревью. 
### Структура файлов проекта
в папке tests:
    файл [test_create_courier.py] http://qa-scooter.praktikum-services.ru/api/v1/courier
    test_create_courier_positive_result - Успешное создание курьера
    test_create_courier_without_login_negative_result - Создание курьера без логина
    test_create_courier_without_password_negative_result - Создание курьера без пароля
    test_create_courier_with_existing_login_negative_result - Создание курьера с повторяющимся логином
    
    файл [test_login_courier.py]
    test_courier_login_return_id - Успешная авторизация возвращает id
    test_courier_login_without_password_negative_result - Авторизация без пароля
    test_courier_login_without_login_negative_result - Авторизация без логина
    test_courier_login_wrong_login_negative_result - Авторизация неверным логином
    test_courier_login_wrong_password_negative_result - Авторизация неверным паролем
    
    файл [test_create_order.py]
    test_create_order_different_colors - Создание заказа в разрезе цвета

    файл [test_check_order_list.py]
    test_list_order - Cписок заказов успешно отображается
