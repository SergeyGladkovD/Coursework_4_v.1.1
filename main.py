from src.api import HeadHunterAPI
from src.JSONSaver import JSONSaver
from src.vacancy import Vacancy


def user_interaction():
    """ Функция для взаимодействия с пользователем. """
    while True:
        user_input = input(f'Хотите посмотреть отложенные вакансии нажмите 1\n'
                           f'Хотите удалить отложенные вакансии нажмите 2\n'
                           f'Хотите начать новый поиск вакансий нажмите 3\n'
                           f'Остальные команды прекратят работу программы.\n')
        if user_input == '1':
            print(JSONSaver.read_vacancy())
        elif user_input == '2':
            JSONSaver.delete_vacancy()
            print('Вакансии удалены.')
        elif user_input == '3':
            current_vacancies = []
            user_input = input('Какую вакансию вы ищете?')
            hh_api = HeadHunterAPI()
            hh_vacancies = hh_api.get_vacancies(user_input)
            user_city = input('В каком городе?')
            # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
            # salary_range = input("Введите диапазон зарплат: ")
            for vacancy in hh_vacancies:
                if vacancy['area']['name'] == user_city:
                    x = Vacancy(vacancy["name"], vacancy["url"], vacancy["salary"], vacancy["snippet"])
                    json_var = {"name": x.name, "vacancy": x.url, "salary": x.salary, "snippet": x.snippet}
                    current_vacancies.append(json_var)
            JSONSaver.add_vacancy(current_vacancies)
        else:
            print('Программа завершена.')
            break


if __name__ == "__main__":
    user_interaction()
