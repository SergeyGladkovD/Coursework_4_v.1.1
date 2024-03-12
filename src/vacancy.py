from abc import ABC
import json


class AbsVacancy(ABC):

    def __init__(self):
        pass

    def to_json(self):
        pass

    def compare_vacancy(self):
        pass


class Vacancy(AbsVacancy):

    def __init__(self, name, url, salary, snippet):
        self.name = name
        self.url = url
        self.snippet = snippet['requirement']
        if salary is None:
            self.salary = 'Зарплата не указана.'
        elif salary['from'] is None:
            self.salary = salary['to']
        elif salary['to'] is None:
            self.salary = salary['from']
        else:
            self.salary = (int(salary['from']) + int(salary['to'])) / 2

    def to_json(self):
        """ Возвращает экземпляр класса как JSON файл. """
        return json.dumps(vars(self), ensure_ascii=False)

    def compare_vacancy(self):
        """ Сравнивает вакансии. """
        pass
