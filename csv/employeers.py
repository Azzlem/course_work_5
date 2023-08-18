import requests
import psycopg2


# Класс получения работодателей по региону 2(Санкт-Петербург) у которых есть открытые вакансии и записи в таблицу БД
class Employers:
    @classmethod
    def get_employers(cls, page=0):
        """
        Получение одной страницы работодателей
        """
        params = {
            'area': 2,  # Поиск в зоне
            'page': page,  # Номер страницы
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        req = requests.get('https://api.hh.ru/employers', params=params)

        return req.json()['items']

    @classmethod
    def page_to_list(cls):
        """
        Цикл из 20 возможных страниц на HH
        """
        temp = []
        for page in range(0, 20):
            list_page = Employers.get_employers(page)
            temp.append(list_page)

        return temp

    @classmethod
    def make_table(cls):
        employers = sum(Employers.page_to_list(), [])

        # создание коннекта
        conn = psycopg2.connect(
            host="localhost",
            database="north",
            user="abc",
            password="abc"
        )
        cur = conn.cursor()

        cur.execute("""
            create table employers
            (
            employer_id int primary key,
            name varchar(200),
            url varchar(200)
            )

        """)

        for employer in employers:
            if int(employer['open_vacancies']) > 5:
                cur.execute(
                    f"insert into employers values(%s, %s, %s)", [
                        employer["id"],
                        employer["name"],
                        employer["alternate_url"]
                    ]
                )
        # запись в бд
        conn.commit()

        # Закрытие коннекта
        cur.close()
        conn.close()



