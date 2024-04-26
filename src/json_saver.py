import json
from abc import ABC, abstractmethod


class VacancyStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass


class VacancySaver(VacancyStorage):
    def __init__(self, filename):
        self.filename = filename
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy)

    #
    def get_vacancies(self, criteria):
        filtered_vacancies = [vacancy for vacancy in self.vacancies if criteria in vacancy.values()]
        return filtered_vacancies

    def delete_vacancy(self, vacancy_id):
        self.vacancies = [vacancy for vacancy in self.vacancies if vacancy.get('id') != vacancy_id]

    def vacancies_to_json(self, vacancies):
        with open(self.filename, 'w') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

