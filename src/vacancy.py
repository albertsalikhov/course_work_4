import json


class Vacancy:
    def __init__(self, name, vacancies_url, salary, short_description):
        self.name = name
        self.vacancies_url = vacancies_url
        self.salary = salary
        self.short_description = short_description
        # self.cast_to_object_list()

    @staticmethod
    def cast_to_object_list(vacancy_list):
        """Преобразование набора данных из JSON в список объектов"""
        vacancy_json_objects = []  # список JSON-объектов, с которыми можно работать
        for vacancy_data in vacancy_list:
            vacancy_json_string = json.dumps(vacancy_data)  # Преобразовать словарь в строку JSON
            vacancy_json_object = json.loads(vacancy_json_string)  # Загрузить строку JSON как объект Python
            vacancy_json_objects.append(vacancy_json_object)
        return vacancy_json_objects

            # print(vacancy['name'])
            # print(vacancy['alternate_url'])
            # try:
            #     print(vacancy['salary']['from'])
            # except:
            #     print('---')
            # try:
            #     print(vacancy['salary']['to'])
            # except:
            #     print('--')
            # print(vacancy['snippet']['requirement'])



# vacancy_list = {'id': '96497148', 'premium': False, 'name': 'Главный специалист', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '2', 'name': 'Санкт-Петербург', 'url': 'https://api.hh.ru/areas/2'}, 'salary': None, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-04-09T09:58:00+0300', 'created_at': '2024-04-09T09:58:00+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=96497148', 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/96497148?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/96497148', 'relations': [], 'employer': {'id': '104628', 'name': 'Газпром', 'url': 'https://api.hh.ru/employers/104628', 'alternate_url': 'https://hh.ru/employer/104628', 'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/333051.jpeg', '240': 'https://img.hhcdn.ru/employer-logo/405908.jpeg', 'original': 'https://img.hhcdn.ru/employer-logo-original/208765.JPG'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=104628', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Навыки обработки, анализа и визуализации данных при помощи BI инструментов (Power BI, Apache Superset) или языков программирования (R и <highlighttext>Python</highlighttext>). – ', 'responsibility': 'Главный специалист (отдел коммерч-ой экспертизы управленческих решений по сбыту товарной продукции). – Проведение экспертизы и оценка экономического эффекта от заключения...'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '134', 'name': 'Финансовый аналитик, инвестиционный аналитик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}
# print(vacancy_list['name'])
# print(vacancy_list['alternate_url'])
# print(vacancy_list['working_time_intervals'], ["name"])
# print(vacancy_list['name'])

# print(type(vacancy_list))
# vacancy = Vacancy.cast_to_object_list(vacancy_list)
