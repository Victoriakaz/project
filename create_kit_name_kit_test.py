from sender_stand_request import *
from data import *
auth_token = get_new_user_token()


def get_kit_body(name):
    return {"name": name}

def positive_result(kit_body):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_result_code_400(kit_body):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

#1.Допустимое количество символов (1):
def test_valid_name_1_symbol():
    positive_result(kit_body_1_symbol)

#2.Допустимое количество символов (511):
def test_valid_name_511_symbol():
    positive_result(kit_body_511_symbol)

#3.Количество символов меньше допустимого (0):
def test_invalid_name_0_symbol():
    negative_result_code_400(kit_body_0_symbol)

#4.Количество символов больше допустимого (512):
def test_invalid_name_512_symbol():
    negative_result_code_400(kit_body_512_symbol)
#5.Разрешены английские буквы:
def test_valid_name_english_symbol():
    positive_result(kit_body_english_symbol)
#6.Разрешены русские буквы:
def test_valid_name_russian_symbol():
    positive_result(kit_body_russian_symbol)
#7.Разрешены спецсимволы:
def test_valid_name_special_symbol():
    positive_result(kit_body_special_symbol)
#8.Разрешены пробелы:
def test_valid_name_spaces():
    positive_result(kit_body_spaces)
#9.Разрешены цифры:
def test_valid_name_numbers():
    positive_result(kit_body_numbers)
#10.Параметр не передан в запросе:
def test_invalid_name_not_provided():
    negative_result_code_400(kit_body_not_provided)
#11.Передан другой тип параметра (число):
def test_invalid_name_wrong_type():
    negative_result_code_400(kit_body_wrong)