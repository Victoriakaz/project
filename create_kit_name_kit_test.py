import pytest
import requests  # Предполагаем, что вы используете requests для отправки запросов
from data import get_new_user_token  # Импортируем функцию для получения токена

def get_kit_body(name):
    return {"name": name}

def positive_assert(kit_body):
    response = requests.post("URL_вашего_API", json=kit_body, headers={"Authorization": f"Bearer {get_new_user_token()}"})
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = requests.post("URL_вашего_API", json=kit_body, headers={"Authorization": f"Bearer {get_new_user_token()}"})
    assert response.status_code == 400

def test_minimum_characters():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

def test_maximum_characters():
    kit_body = get_kit_body("Тестовое значение для этой проверки будет ниже")
    positive_assert(kit_body)

def test_empty_name():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

def test_too_long_name():
    kit_body = get_kit_body("A" * 513)  # 513 символов
    negative_assert_code_400(kit_body)

def test_english_letters():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body)

def test_russian_letters():
    kit_body = get_kit_body("Маша")
    positive_assert(kit_body)

def test_special_characters():
    kit_body = get_kit_body("№%@,")
    positive_assert(kit_body)

def test_spaces():
    kit_body = get_kit_body(" Человек и КО ")
    positive_assert(kit_body)

def test_numbers():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

def test_missing_parameter():
    kit_body = {}
    negative_assert_code_400(kit_body)

def test_invalid_parameter_type():
    kit_body = get_kit_body(123)  # Передаем число вместо строки
    negative_assert_code_400(kit_body)

# Тестовые значения для проверок №2 и №4
def test_maximum_characters_test_value():
    kit_body = get_kit_body("Abcd" * 127)  # 511 символов
    positive_assert(kit_body)

def test_too_long_name_test_value():
    kit_body = get_kit_body("Abcd" * 128)  # 512 символов
    negative_assert_code_400(kit_body)