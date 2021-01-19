# Сервис для управления номерами отелей и бронированиями

Тестовое задание [Backend-стажёр в юнит Авито.Недвижимость](https://github.com/avito-tech/verticals/blob/master/trainee/backend-str.md).  

Сервис реализован на Python 3.8.

Использованы фреймворки:
Django 3.1;
Django Rest Framework 3.12.

База данных PostgreSQL.

Сервис опубликован: https://manage-hotel.herokuapp.com/

## 1. Сервис имеет следующие хендлеры для работы с каталогом номеров отеля:
* **Добавить номер отеля.** Принимает на вход текстовое описание и цену за ночь. Возвращает ID номера отеля

    Пример запроса:
    ```shell script
    curl -X POST -d "description=одноместный номер Люкс" -d "price=5000" http://localhost:8000/rooms/
    ```
    Ответ:
    ```shell script
    {"room_id":10}
    ```

* **Удалить номер отеля и все его брони.** Принимает на вход ID номера отеля.
 
    Пример запроса:
    ```shell script
    curl -X DELETE -d "room_id=5" http://localhost:8000/rooms/
    ```
    Ответ:
    ```shell script
    "room id 5 deleted"
    или
    "room id 5 not found"
    ```
  
 * **Получить список номеров отеля.** Номера выводятся отсортированные по цене.
 
     Пример запроса:
    ```shell script
    curl -X GET http://localhost:8000/rooms/
    ```
    Ответ:
    ```shell script
    [{"id":4,"description":"test","price":"100.00"},{"id":3,"description":"Эконом +","price":"5000.00"}]
    ```

## 2. Сервис имеет следующие хендлеры для работы со списком броней номеров:

 * **Добавить бронь.** Принимает на вход существующий ID номера отеля, дату начала, дату окончания брони. Возвращает ID брони.
    
    Пример запроса:
    ```shell script
    curl -X POST -d "room_id=6" -d "date_start=2021-12-30" -d "date_end=2022-01-02" http://localhost:8000/booking/create/
    ```
    Ответ:
    ```shell script
    {"booking_id":10}
    ```
  
  * **Удалить бронь.** Принимает на вход ID брони.
  
    Пример запроса:
    ```shell script
    curl -X DELETE -d "booking_id=10" http://localhost:8000/room/id=6/bookings/
    ```
    Ответ:
    ```shell script
    "booking id 10 deleted"
    или
    "booking id 10 not found"
    ```
  * **Получить список броней номера отеля.** Принимает на вход ID номера отеля. Возвращает список бронирований. 
  Бронирования отсортированы по дате начала.
    Пример запроса:
    ```shell script
    curl -X GET http://localhost:8000/room/id=3/bookings/
    ```
    Ответ:
    ```shell script
    [{"id":11,"date_start":"2021-01-17","date_end":"2021-01-17"},{"id":12,"date_start":"2021-01-22","date_end":"2021-01-24"}]
    ```

## Установка проекта.
1. [Установить Python.](https://www.python.org/downloads/)
2. Скачать проект.
3. Создать виртуальное окружение: python -m venv env
4. Активировать виртуальное окружение: source env/scripts/activate
5. Установить зависимости: pip install -r requirements.txt
6. Создать базу данных и указать данные в файле settings.py DATABASES
7. Запустить проект: ./manage.py runserver
8. Открыть в браузере: http://localhost:8000.

PS: в ближайшее время будут добавлены юнит-тесты.