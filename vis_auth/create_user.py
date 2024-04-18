import requests

url = 'http://localhost:8000/api/register/'

role = ''

while role != "Линкольн" and role != "Дуглас" and role != "Lincoln" and role != "Duoglas":
    role = input("Введите вашу роль КОРРЕКТНО ")

data = {
    'name': input("Введите ваше имя "),
    'email': input("Введите вашу почту "),
    'password': input("Введите пароль "),
    'role': role
}

response = requests.post(url, json=data)
print(response.text)