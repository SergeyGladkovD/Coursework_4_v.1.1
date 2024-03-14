from abc import ABC


class AbsVacancy(ABC):

    def __init__(self):
        pass

    def valid_salary(self, **kwargs):
        pass

    def compare_vacancy(self):
        pass


class Vacancy(AbsVacancy):

    def __init__(self, name: str, url: str, salary: float or int, snippet: dict):
        super().__init__()
        self.name = name
        self.url = url
        self.snippet = snippet['requirement']
        self.salary = Vacancy.valid_salary(salary)

    @staticmethod
    def valid_salary(salary: dict) -> float:
        if salary is None:
            salary = 0
        elif salary['from'] is None:
            salary = salary['to']
        elif salary['to'] is None:
            salary = salary['from']
        else:
            salary = (int(salary['from']) + int(salary['to'])) / 2
        return salary

    def compare_vacancy(self):
        """ Сравнивает вакансии. """
        pass
