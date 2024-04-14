import json


class Vacancy:
    def __init__(self, name, vacancies_url, salary, short_description):
        self.name = name
        self.vacancies_url = vacancies_url
        self._salary = salary
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

    @property
    def get_salary(self):
        return self._salary

    @get_salary.setter
    def get_salary(self, salary):
        if not self._salary:
            print('Зарплата не указана')
        self._salary = salary

    def comparison_vacancies(self, other_vacancy):
        if self._salary > other_vacancy.salary:
            return f"{self.name} имеет большую зарплату, чем {other_vacancy.name}"
        elif self._salary < other_vacancy.salary:
            return f"{self.name} имеет меньшую зарплату, чем {other_vacancy.name}"
        else:
            return "Зарплата у вакансий одинаковая"



    # def __str__(self):
    #     return f'{self.name}', {self.vacancies_url}, {self.salary}, {self.short_description}



