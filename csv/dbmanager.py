import pprint

import psycopg2
import json


class DBManager:
    # создание коннекта
    @staticmethod
    def get_companies_and_vacancies_count():
        conn = psycopg2.connect(
            host="localhost",
            database="north",
            user="abc",
            password="abc"
        )
        cur = conn.cursor()

        cur.execute("""
        select employers.name, count(*) as vacancies_count
        from employers
        join vacancies using(employer_id)
        group by employer_id;
        """)
        temp = [el for el in cur]

        # Закрытие коннекта
        cur.close()
        conn.close()
        return temp

    @staticmethod
    def get_all_vacancies():
        conn = psycopg2.connect(
            host="localhost",
            database="north",
            user="abc",
            password="abc"
        )
        cur = conn.cursor()

        cur.execute("""
        select employers.name, vacancies.name, vacancies.salary, vacancies.url
        from employers
        join vacancies using(employer_id);
        """)
        temp = [el for el in cur]

        # Закрытие коннекта
        cur.close()
        conn.close()
        return temp

    @staticmethod
    def get_avg_salary():
        conn = psycopg2.connect(
            host="localhost",
            database="north",
            user="abc",
            password="abc"
        )
        cur = conn.cursor()

        cur.execute("""
                select avg(salary)
                from vacancies;
                """)
        temp = [el for el in cur]

        # Закрытие коннекта
        cur.close()
        conn.close()
        return temp[0][0]

    @staticmethod
    def get_vacancies_with_higher_salary():
        conn = psycopg2.connect(
            host="localhost",
            database="north",
            user="abc",
            password="abc"
        )
        cur = conn.cursor()

        cur.execute(f"select * from vacancies where salary > {DBManager.get_avg_salary()}")
        temp = [el for el in cur]

        # Закрытие коннекта
        cur.close()
        conn.close()
        return temp

    @staticmethod
    def get_vacancies_with_keyword(user_input):
        conn = psycopg2.connect(
            host="localhost",
            database="north",
            user="abc",
            password="abc"
        )
        cur = conn.cursor()

        cur.execute(f"select * from vacancies where vacancies.name like '%{user_input}%'")
        temp = [el for el in cur]

        # Закрытие коннекта
        cur.close()
        conn.close()
        return temp



