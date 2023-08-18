import psycopg2
from csv.dbmanager import DBManager


def drop_table():
    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="abc",
        password="abc"
    )
    cur = conn.cursor()

    cur.execute("""
    DROP TABLE  IF EXISTS  vacancies CASCADE;
    DROP TABLE  IF EXISTS  employers CASCADE;
    """)
    conn.commit()

    # Закрытие коннекта
    cur.close()
    conn.close()


class LaconicOutputToUser:
    @staticmethod
    def laconic_avg():
        temp = DBManager.get_avg_salary()
        return f"Средняя зарплата всех вакансий {round(temp, 0)} рублей.\n"

    @staticmethod
    def laconic_companies_and_vacancies_count():
        temp = DBManager.get_companies_and_vacancies_count()
        total = ""
        for el in temp:
            total += f"{el[0]}, {el[1]} вакансий.\n"
        return total

    @staticmethod
    def laconic_all_vacancies():
        temp = DBManager.get_all_vacancies()
        total = ""
        for el in temp:
            if el[2] is None:
                total += f"{el[0]}, {el[1]}, зарплата не указана, {el[3]} \n"
            else:
                total += f"{el[0]}, {el[1]}, зарплата от {el[2]}, {el[3]} \n"
        return total

    @staticmethod
    def laconic_vacancies_with_higher_salary():
        temp = DBManager.get_vacancies_with_higher_salary()
        total = ""
        for el in temp:
            if el[4] is None:
                total += f"ID_ваканчии: {el[0]}, {el[1]}, ID_работодателя: {el[3]}, {el[2]}, Зарплата не указана.\n"
            else:
                total += f"ID_вакансии: {el[0]}, {el[1]}, ID_работодателя: {el[3]}, {el[2]}, Зарплата: {el[4]}\n"
        return total

    @staticmethod
    def laconic_get_vacancies_with_keyword():
        temp = DBManager.get_vacancies_with_keyword(input("Введите слово для поиска: ").capitalize())
        total = ""
        for el in temp:
            if el[4] is None:
                total += f"ID_ваканчии: {el[0]}, {el[1]}, ID_работодателя: {el[3]}, {el[2]}, Зарплата не указана.\n"
            else:
                total += f"ID_вакансии: {el[0]}, {el[1]}, ID_работодателя: {el[3]}, {el[2]}, Зарплата: {el[4]}\n"
        return total
