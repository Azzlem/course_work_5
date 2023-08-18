from csv.dbmanager import DBManager
from employeers import Employers
from vacancies import Vacancies
print("Please Wait")
Employers.make_table()
Vacancies.make_table()
print("Bases successfully makes")


print(DBManager.get_vacancies_with_higher_salary())
print(DBManager.get_avg_salary())
print(DBManager.get_companies_and_vacancies_count())
print(DBManager.get_all_vacancies())
print(DBManager.get_vacancies_with_keyword(input("Введите запрос: ").capitalize()))


