import json


class Vacancy:
    def __init__(self, name, vacancies_url, salary_from, salary_to, short_description):
        self.name = name
        self.vacancies_url = vacancies_url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.short_description = short_description

    @staticmethod
    def cast_to_object_list(vacancy_list):
        """Преобразование набора данных JSON в список объектов"""
        vacancy_objects = []
        for vacancy_data in vacancy_list:
            vacancy = Vacancy.from_dict(vacancy_data)
            vacancy_objects.append(vacancy)
        return vacancy_objects

    def comparison_vacancies(self, other_vacancy):
        """ Сравниваем зарплаты текущей вакансии с зарплатами другой вакансии
        и возвращаем информацию о результатах сравнения."""
        if self.salary_to > other_vacancy.salary_to:
            return f"{self.name} имеет большую зарплату, чем {other_vacancy.name}"
        elif self.salary_to < other_vacancy.salary_to:
            return f"{self.name} имеет меньшую зарплату, чем {other_vacancy.name}"
        else:
            if self.salary_from > other_vacancy.salary_from:
                return f"{self.name} имеет большую начальную зарплату, чем {other_vacancy.name}"
            elif self.salary_from < other_vacancy.salary_from:
                return f"{self.name} имеет меньшую начальную зарплату, чем {other_vacancy.name}"
            else:
                return "Зарплата у вакансий одинаковая"

    @classmethod
    def from_dict(cls, vacancy_dict):
        """Создаем экземпляр класса на основе словаря vacancy_dict"""
        salary_from = 0
        salary_to = 0

        if 'salary' in vacancy_dict:
            salary_info = vacancy_dict['salary']
            if salary_info is not None:
                salary_from = salary_info.get('from')
                salary_to = salary_info.get('to')

        return cls(
            name=vacancy_dict.get('name'),
            vacancies_url=vacancy_dict.get('apply_alternate_url'),
            salary_from=salary_from,
            salary_to=salary_to,
            short_description=vacancy_dict.get('snippet', {}).get('requirement')
            )

    def to_dict(self):
        """Преобразуем экземпляр класса в словарь, содержащий информацию об этом экземпляре в формате,
         удобном для передачи или сохранения данных."""
        vacancy_dict = {
            'name': self.name,
            'vacancies_url': self.vacancies_url,
            'salary': {
                'from': self.salary_from,
                'to': self.salary_to
            },
            'snippet': {
                'requirement': self.short_description
            }
        }
        return vacancy_dict

    def __str__(self):
        return f'{self.name}, {self.vacancies_url}, {self.salary_from}, {self.salary_to}, {self.short_description}'


