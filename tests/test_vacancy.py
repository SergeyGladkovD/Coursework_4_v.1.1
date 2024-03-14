from src.vacancy import Vacancy
import pytest


@pytest.fixture()
def random_vacancy():
    return Vacancy("Охранник (склад)", "https://hh.ru/vacancy/94508038", None,
                   {"requirement": "Знание системы работы видеонаблюдения. Внимательность. Ответственность."})


def test_init(random_vacancy):
    assert random_vacancy.name == "Охранник (склад)"
    assert random_vacancy.url == "https://hh.ru/vacancy/94508038"
    assert random_vacancy.salary == 0
    assert random_vacancy.snippet == "Знание системы работы видеонаблюдения. Внимательность. Ответственность."


def test_valid_salary():
    assert Vacancy.valid_salary(None) == 0
    assert Vacancy.valid_salary({"from": 1000, "to": None}) == 1000
    assert Vacancy.valid_salary({"from": None, "to": 500}) == 500
    assert Vacancy.valid_salary({"from": 1000, "to": 500}) == 750
