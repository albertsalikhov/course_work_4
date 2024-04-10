import requests

url_get = "https://httpbin.org/get" # используемый адрес для отправки запроса

response = requests.get(url_get) # отправка GET-запроса

print(response) # вывод объекта класса Response
# Вывод:
# >> <Response [200]>

print(response.status_code) # вывод статуса запроса, 200 означает, что всё хорошо, остальные коды нас пока не интересуют и их можно считать показателем ошибки
# Вывод:
# >> 200

print(response.text) # печать ответа в виде текста того, что вернул нам внешний сервис
# Вывод:
