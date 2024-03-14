from src.JSONSaver import JSONSaver
from src.api import HeadHunterAPI
from src.vacancy import Vacancy


def user_interaction():
    """ Функция для взаимодействия с пользователем. """
    while True:
        user_input = input(f'Хотите посмотреть отложенные вакансии нажмите 1\n'
                           f'Хотите удалит старый список и начать новый поиск вакансий нажмите 2\n'
                           f'Остальные команды прекратят работу программы.\n')
        if user_input == '1':
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            print(JSONSaver.read_vacancy(top_n))
        elif user_input == '2':
            JSONSaver.delete_vacancy()
            current_vacancies = []
            user_input = input('Какую вакансию вы ищете? ')
            hh_vacancies = HeadHunterAPI.get_vacancies(user_input)
            user_city = input('В каком городе? ')
            for vacancy in hh_vacancies:
                if vacancy['area']['name'] == user_city:
                    x = Vacancy(vacancy["name"], vacancy["alternate_url"], vacancy["salary"], vacancy["snippet"])
                    json_var = {"name": x.name, "vacancy": x.url, "salary": x.salary, "snippet": x.snippet}
                    current_vacancies.append(json_var)
            JSONSaver.add_vacancy(current_vacancies)
        else:
            print('Программа завершена.')
            break


if __name__ == "__main__":
    user_interaction()
