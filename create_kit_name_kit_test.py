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
    kit_body = get_kit_body("a")
    positive_result(kit_body)


#2.Допустимое количество символов (511):
def test_valid_name_511_symbol():
    kit_body = get_kit_body(
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabC"
    )
    positive_result(kit_body)

#3.Количество символов меньше допустимого (0):
def test_invalid_name_0_symbol():
    kit_body = get_kit_body("")
    negative_result_code_400(kit_body)

#4.Количество символов больше допустимого (512):
def test_invalid_name_512_symbol():
    kit_body = get_kit_body(
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcD"
    )
    negative_result_code_400(kit_body)
#5.Разрешены английские буквы:
def test_valid_name_english_symbol():
    kit_body = get_kit_body("QWErty")
    positive_result(kit_body)
#6.Разрешены русские буквы:
def test_valid_name_russian_symbol():
    kit_body = get_kit_body("Мария")
    positive_result(kit_body)
#7.Разрешены спецсимволы:
def test_valid_name_special_symbol():
    kit_body = get_kit_body('"№%@,')
    positive_result(kit_body)
#8.Разрешены пробелы:
def test_valid_name_spaces():
    kit_body = get_kit_body(" Человек и КО ")
    positive_result(kit_body)
#9.Разрешены цифры:
def test_valid_name_numbers():
    kit_body = get_kit_body("123")
    positive_result(kit_body)
#10.Параметр не передан в запросе:
def test_invalid_name_not_provided():
    kit_body = get_kit_body(None)
    assert kit_body == {}  
    negative_result_code_400(kit_body)
#11.Передан другой тип параметра (число):
def test_invalid_name_wrong_type():
    kit_body = get_kit_body(123)
    negative_result_code_400(kit_body)

