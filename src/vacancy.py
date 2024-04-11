import json


class Vacancy:
    def __init__(self, name, vacancies_url, salary, short_description):
        self.name = name
        self.vacancies_url = vacancies_url
        self.salary = salary
        self.short_description = short_description

    @staticmethod
    def cast_to_object_list(vacancy_list):
        """Преобразование набора данных из JSON в список объектов"""
        vacancy_json_objects = []  # список JSON-объектов, с которыми можно работать
        for vacancy_data in vacancy_list:
            vacancy_json_string = json.dumps(vacancy_data)  # Преобразовать словарь в строку JSON
            vacancy_json_object = json.loads(vacancy_json_string)  # Загрузить строку JSON как объект Python
            vacancy_json_objects.append(vacancy_json_object)
        return vacancy_json_objects

