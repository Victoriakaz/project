import requests
import json
import configuration  # Импортируем файл с конфигурацией для получения токена
from data import new_kit_body, kit_body_with_card  # Импортируем данные из data.py

def post_new_client_kit(kit_body, auth_token=None, card_id=None):
    # URL API для создания нового набора
    API_URL = "https://bcea6c2e-33d9-4ceb-a3c7-32301319a085.serverhub.praktikum-services.ru/api/v1/kits"

    # Заголовки
    headers = {
        "Content-Type": "application/json"
    }

    # Добавляем Authorization, если он передан
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"

    # Проверяем, переданы ли необходимые параметры
    if not auth_token and not card_id:
        return {
            "code": 400,
            "message": "Не все необходимые параметры были переданы"
        }

    # Добавляем cardId в тело запроса, если он передан
    if card_id:
        kit_body["cardId"] = card_id

    # Отправка POST-запроса
    response = requests.post(API_URL, headers=headers, json=kit_body)

    # Проверка успешности запроса
    if response.status_code == 201:
        return response.json()  # Возвращаем ответ в формате JSON
    else:
        print(f"Ошибка при создании набора: {response.status_code} - {response.text}")
        return None  # Возвращаем None в случае ошибки


# Пример использования функции
if __name__ == "__main__":
    # Получаем токен из файла конфигурации
    token = configuration.AUTH_TOKEN

    # Вызов функции для создания нового набора (например, только с токеном)
    create_response = post_new_client_kit(new_kit_body, auth_token=token)
    print(create_response)

    # Или, если мы хотим создать набор внутри карточки
    create_response_with_card = post_new_client_kit(kit_body_with_card, auth_token=token)
    print(create_response_with_card)
