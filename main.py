# Функция для фильтрации вакансий по ключевым словам
# Создание экземпляра класса для работы с API сайтов с вакансиями
import json

from src.get_requests import HH
from src.json_saver import VacancySaver
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
from src.vacancy import Vacancy


def user_interaction():  # Функция взаимодействия с пользователем
    search_query = input("Введите поисковый запрос: ")
    # top_n = int(input("Введите количество вакансий, которые будут отображаться в верхней N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий:").split()
    # salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    hh_api = HH()

    hh_vacancies = hh_api.load_vacancies(search_query)  # Получение вакансий с hh.ru в формате JSON
    vacancy_list = hh_api.vacancies # список вакансий

    if vacancy_list is None:
        print("Вакансий не найдено. Пожалуйста, попробуйте еще раз с другим поисковым запросом.")
        return

    vacancies_list = Vacancy.cast_to_object_list(vacancy_list)  # преобразование набора данных JSON в список объектов

    if not vacancies_list:
        print("По данному поисковому запросу вакансий не найдено.")
        return

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    print(filtered_vacancies)
    # for vac in filtered_vacancies:
    #     print(vac)

    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    # # print(ranged_vacancies)
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # print("Top vacancies:")
    # print_vacancies(top_vacancies)


if __name__ == '__main__':
    user_interaction()
