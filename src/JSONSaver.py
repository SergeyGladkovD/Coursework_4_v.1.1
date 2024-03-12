import json
from abc import ABC
import os


class AbsJSONSaver(ABC):

    @staticmethod
    def add_vacancy(**kwargs):
        pass

    @staticmethod
    def delete_vacancy():
        pass

    @staticmethod
    def read_vacancy():
        pass


class JSONSaver(AbsJSONSaver):
    @staticmethod
    def add_vacancy(data):
        """ Сохраняет информацию о вакансиях в файл. """
        with open(os.path.join('data', 'vacancy.json'), 'a', encoding='utf 8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def delete_vacancy():
        """ Удаляет информацию о вакансиях в файле. """
        with open(os.path.join('data', 'vacancy.json'), 'w', encoding='utf 8'):
            pass

    @staticmethod
    def read_vacancy():
        """ Выводит информацию о вакансиях в файле. """
        with open(os.path.join('data', 'vacancy.json'), 'r', encoding='utf 8') as file:
            data = json.load(file)
            sorted_obj = sorted(data, key=lambda x: x['salary'], reverse=True)
            # return sorted_obj
            for i in sorted_obj:
                print(f'Вакансия: {i["name"]}, {i["vacancy"]}, зарплата = {i["salary"]}, требования: {i["snippet"]}')
