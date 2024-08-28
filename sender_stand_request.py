# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data
# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests

#Этот код отправляет HTTP GET-запрос к заданному URL-адресу, который складывается
#из базового адреса сервиса и пути к его документации, оба определены в модуле
#конфигурации. Затем он выводит HTTP-статус код ответа от сервера, который указывает
#на результат выполнения запроса.

# Определяем функцию get_docs, которая не принимает параметров
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


# Определяем функцию get_logs, которая отправляет GET-запрос к серверу для получения логов
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})


# Функция для получения данных из таблицы пользователей
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# Определение функции для отправки POST-запроса на поиск наборов по продуктам
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,  # Тело запроса содержит ID продуктов в формате JSON
                         headers=data.headers)  # Использование заголовков из файла data.py
