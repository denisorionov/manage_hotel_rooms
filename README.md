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
    curl -X POST -d "description=Dorm" -d "price=1000"  https://manage-hotel.herokuapp.com/rooms/
    ```
    Ответ:
    ```shell script
    {"room_id":4}
    ```

* **Удалить номер отеля и все его брони.** Принимает на вход ID номера отеля.
 
    Пример запроса:
    ```shell script
    curl -X DELETE -d "room_id=4" https://manage-hotel.herokuapp.com/rooms/
    ```
    Ответ:
    ```shell script
    "room id 4 deleted"
    если номера с таким id не существует:
    "room id 4 not found"
    ```
  
 * **Получить список номеров отеля.** 
 
     Пример запроса:
    ```shell script
    curl -X GET https://manage-hotel.herokuapp.com/rooms/
    ```
    Ответ:
    ```shell script
    [{"id":4,"description":"test","price":"100.00"},{"id":3,"description":"Эконом +","price":"5000.00"}]
    ```
    Возможна сортировка по цене и id номера. 
    Сортировка по цене:
    ```shell script
    curl -X GET https://manage-hotel.herokuapp.com/rooms/?ordering=price
    ```
   Для сортировки от большей цены к меньшей:
   ```shell script
   curl -X GET https://manage-hotel.herokuapp.com/rooms/?ordering=-price
   ```
    
## 2. Сервис имеет следующие хендлеры для работы со списком броней номеров:

 * **Добавить бронь.** Принимает на вход существующий ID номера отеля, дату начала, дату окончания брони. Возвращает ID брони.
    
    Пример запроса:
    ```shell script
    curl -X POST -d "room_id=6" -d "date_start=2021-12-30" -d "date_end=2022-01-02" https://manage-hotel.herokuapp.com/bookings/ 
    ```
    Ответ:
    ```shell script
    {"booking_id":10}
    ```
  
  * **Удалить бронь.** Принимает на вход ID брони.
  
    Пример запроса:
    ```shell script
    curl -X DELETE -d "booking_id=2" https://manage-hotel.herokuapp.com/bookings/
    ```
    Ответ:
    ```shell script
    "booking id 2 deleted"
    если брони с таким id не существует:
    "booking id 10 not found"
    ```
  * **Получить список броней номера отеля.** Принимает на вход ID номера отеля. Возвращает список бронирований. 
  Бронирования отсортированы по дате начала.
    Пример запроса:
    ```shell script
    curl -X GET https://manage-hotel.herokuapp.com/bookings/?room_id=6
    ```
    Ответ:
    ```shell script
    [{"id":4,"date_start":"2020-12-30","date_end":"2021-01-02"},{"id":3,"date_start":"2021-12-30","date_end":"2022-01-02"}]
    ```

## Установка проекта.
1. [Установить Python.](https://www.python.org/downloads/)
2. Скачать проект.
3. Создать виртуальное окружение: python -m venv env
4. Активировать виртуальное окружение: source env/scripts/activate
5. Установить зависимости: pip install -r requirements.txt
6. Создать базу данных и указать данные в файле settings.py DATABASES
7. Выполнить миграции ./manage.py migrate
8. Запустить проект: ./manage.py runserver
9. Открыть в браузере: http://localhost:8000.
