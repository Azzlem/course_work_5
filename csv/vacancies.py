import psycopg2
import requests


class Vacancies:
    @classmethod
    def get_id_emloyers(cls):
        # создание коннекта
        conn = psycopg2.connect(
            host="localhost",
            database="north",
            user="abc",
            password="abc"
        )
        cur = conn.cursor()

        cur.execute("""
        select employers_id from employers
        """)
        temp = [el[0] for el in cur]

        # Закрытие коннекта
        cur.close()
        conn.close()
        return temp

    @classmethod
    def get_vacancies(cls, employer_id, page=0):
        """
        Получение одной страницы работодателей
        """
        params = {
            'employer_id': employer_id,  # id работодателя
            'area': 2,  # Поиск в зоне
            'page': page,  # Номер страницы
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        req = requests.get('https://api.hh.ru/vacancies', params=params)

        return req.json()['items'] if "items" in req.json().keys() else []

    @classmethod
    def page_to_list(cls):
        """
        Цикл из доступных id работодателей на HH
        """
        employers_id = Vacancies.get_id_emloyers()
        temp = []
        for employer_id in employers_id:
            list_page = Vacancies.get_vacancies(employer_id)
            temp.append(list_page)

        return temp

    @classmethod
    def make_table(cls):
        vacancies = sum([value for value in Vacancies.page_to_list() if value], [])

        # создание коннекта
        conn = psycopg2.connect(
            host="localhost",
            database="north",
            user="abc",
            password="abc"
        )
        cur = conn.cursor()

        cur.execute("""
                create table vacancies
                (
                employers_id int,
                name varchar(200),
                url varchar(200)
                )

            """)

        for vacancie in vacancies:
            cur.execute(
                f"insert into vacancies values(%s, %s, %s)", [
                    vacancie["id"],
                    vacancie["name"],
                    vacancie["alternate_url"]
                ]
            )

        # запись в бд
        conn.commit()

        # Закрытие коннекта
        cur.close()
        conn.close()


Vacancies.make_table()
