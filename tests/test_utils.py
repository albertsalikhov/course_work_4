import pytest

from src.utils import filter_vacancies, sort_vacancies
from src.vacancy import Vacancy


@pytest.fixture
def vacancies():
    return [
        Vacancy(name='Python dev', vacancies_url='url 1', short_description='Short Description 1',
                salary_from=80000, salary_to=120000),
        Vacancy(name='Java dev', vacancies_url='url 2', short_description='Short Description 2',
                salary_from=60000, salary_to=None),
        Vacancy(name='Go dev', vacancies_url='url 3', short_description='Short Description 3',
                salary_from=None, salary_to=150000)
    ]


def test_sort_vacancies(vacancies):
    sorted_vacancies = sort_vacancies(vacancies)

    expected_result = [
        Vacancy(name='Go dev', vacancies_url='url 3', short_description='Short Description 3',
                salary_from=None, salary_to=150000),
        Vacancy(name='Python dev', vacancies_url='url 1', short_description='Short Description 1',
                salary_from=80000, salary_to=120000),
        Vacancy(name='Java dev', vacancies_url='url 2', short_description='Short Description 2',
                salary_from=60000, salary_to=None)
    ]

    assert sorted_vacancies == expected_result


