from src.get_requests import HH
from src.json_saver import VacancySaver
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
from src.vacancy import Vacancy
import os

data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)


def user_interaction():  # Функция взаимодействия с пользователем
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий:").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    hh_api = HH()

    hh_vacancies = hh_api.load_vacancies(search_query)  # Получение вакансий с hh.ru в формате JSON
    vacancy_list = hh_vacancies # список вакансий
    saver = VacancySaver(os.path.join(data_dir, 'vacancies_list.json'))
    saver.vacancies_to_json(vacancy_list)
    # saver = VacancySaver('vacancies_list.json')
    # saver.vacancies_to_json(vacancy_list)   # сохраняет список вакансий по поисковому запросу

    if vacancy_list is None:
        print("Вакансий не найдено. Пожалуйста, попробуйте еще раз с другим поисковым запросом.")
        return

    vacancies_list = Vacancy.cast_to_object_list(vacancy_list)  # преобразование набора данных JSON в список объектов

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    quantity_vacancies = len(sorted_vacancies)
    print(f'\nКоличество отобранных вакансий {quantity_vacancies}')
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print(f"\nТоп вакансий:{top_n}")
    for vacancy in top_vacancies:
        print(f'\n{vacancy}')

    saver = VacancySaver(os.path.join(data_dir, 'top_vacancies.json'))
    vacancy_data = []
    for vacancy in top_vacancies:
        vacancy_data.append(vacancy.to_dict())
    saver.vacancies_to_json(vacancy_data)

    # saver = VacancySaver('top_vacancies.json')
    # vacancy_data =[]
    # for vacancy in top_vacancies:
    #     vacancy_data.append(vacancy.to_dict())
    # saver.vacancies_to_json(vacancy_data)  # сохраняем топ список вакансий

    # print("Топ вакансий:\n")
    # print_vacancies(top_vacancies)  # выводит топ вакансий


if __name__ == '__main__':
    user_interaction()
