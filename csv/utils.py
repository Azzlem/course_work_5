# imports
import psycopg2
from csv.dbmanager import DBManager


# Function to delete database tables
def drop_table(cur, conn):
    cur.execute("""
    DROP TABLE  IF EXISTS  vacancies CASCADE;
    DROP TABLE  IF EXISTS  employers CASCADE;
    """)
    conn.commit()

    # Закрытие коннекта
    cur.close()
    conn.close()


# Class of concise and beautiful information output to the user in the console
class LaconicOutputToUser:
    @staticmethod
    def laconic_avg(cur):
        temp = DBManager.get_avg_salary(cur)
        return f"Средняя зарплата всех вакансий {round(temp, 0)} рублей.\n"

    @staticmethod
    def laconic_companies_and_vacancies_count(cur):
        temp = DBManager.get_companies_and_vacancies_count(cur)
        total = ""
        for el in temp:
            total += f"{el[0]}, {el[1]} вакансий.\n"
        return total

    @staticmethod
    def laconic_all_vacancies(cur):
        temp = DBManager.get_all_vacancies(cur)
        total = ""
        for el in temp:
            if el[2] is None:
                total += f"{el[0]}, {el[1]}, зарплата не указана, {el[3]} \n"
            else:
                total += f"{el[0]}, {el[1]}, зарплата от {el[2]}, {el[3]} \n"
        return total

    @staticmethod
    def laconic_vacancies_with_higher_salary(cur):
        temp = DBManager.get_vacancies_with_higher_salary(cur)
        total = ""
        for el in temp:
            if el[4] is None:
                total += f"ID_ваканчии: {el[0]}, {el[1]}, ID_работодателя: {el[3]}, {el[2]}, Зарплата не указана.\n"
            else:
                total += f"ID_вакансии: {el[0]}, {el[1]}, ID_работодателя: {el[3]}, {el[2]}, Зарплата: {el[4]}\n"
        return total

    @staticmethod
    def laconic_get_vacancies_with_keyword(cur):
        temp = DBManager.get_vacancies_with_keyword(input("Введите слово для поиска: ").capitalize(), cur)
        total = ""
        for el in temp:
            if el[4] is None:
                total += f"ID_ваканчии: {el[0]}, {el[1]}, ID_работодателя: {el[3]}, {el[2]}, Зарплата не указана.\n"
            else:
                total += f"ID_вакансии: {el[0]}, {el[1]}, ID_работодателя: {el[3]}, {el[2]}, Зарплата: {el[4]}\n"
        return total
