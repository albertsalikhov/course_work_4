

def filter_vacancies(vacancies, filter_words):
    """Фильтрует список вакансий по заданным ключевым словам"""
    filtered_vacancies = []
    for vacancy in vacancies:
        vacancy_name_lower = vacancy.name.lower()
        for word in filter_words:
            if word in vacancy_name_lower:
                filtered_vacancies.append(vacancy)
                break
    return filtered_vacancies


def get_vacancies_by_salary(vacancies, salary_range):
    """Метод для извлечения вакансий из списка, которые соответствуют заданному диапазону зарплат"""
    try:
        min_salary, max_salary = map(int, salary_range.split('-'))
    except ValueError:
        print("Неверный формат диапазона зарплат. Используйте формат 'минимум-максимум'.")
        return []

    filtered_vacancies = []
    for vacancy in vacancies:
        salary_from = vacancy.salary_from
        salary_to = vacancy.salary_to

        if salary_from is not None and salary_to is not None:
            if min_salary <= salary_from <= max_salary or min_salary <= salary_to <= max_salary:
                filtered_vacancies.append(vacancy)
        elif salary_from is not None:
            if min_salary <= salary_from <= max_salary:
                filtered_vacancies.append(vacancy)
        elif salary_to is not None:
            if min_salary <= salary_to <= max_salary:
                filtered_vacancies.append(vacancy)

    return filtered_vacancies


def sort_vacancies(vacancies):
    """Функция для сортировки вакансий по убыванию зарплаты"""
    return sorted(vacancies, key=lambda x: x.salary_to if x.salary_to is not None else x.salary_from, reverse=True)


def get_top_vacancies(vacancies, top_n):
    """Функция для получения топ N вакансий"""
    return vacancies[:top_n]


def print_vacancies(vacancies):
    """Функция для вывода информации о вакансиях"""
    for vacancy in vacancies:
        print(f"Название: {vacancy.name}")
        print(f"Зарплата от: {vacancy.salary_from}")
        print(f"Зарплата до: {vacancy.salary_to}")
        print(f"Ссылка: {vacancy.vacancies_url}")
        if vacancy.short_description is not None:
            cleaned_text_description = vacancy.short_description.replace("<highlighttext>", "").replace("</highlighttext>", "")
            print(f"Краткое описание: {cleaned_text_description}\n")
