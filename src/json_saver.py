import json


class VacancySaver:
    def __init__(self, filename):
        self.filename = filename

    def save_vacancies_to_json(self, vacancies):
        with open(self.filename, 'w') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

