import psycopg2


# Database query class
class DBManager:
    @staticmethod
    def get_companies_and_vacancies_count(cur):
        cur.execute("""
        select employers.name, count(*) as vacancies_count
        from employers
        join vacancies using(employer_id)
        group by employer_id;
        """)
        temp = [el for el in cur]

        return temp

    @staticmethod
    def get_all_vacancies(cur):
        cur.execute("""
        select employers.name, vacancies.name, vacancies.salary, vacancies.url
        from employers
        join vacancies using(employer_id);
        """)
        temp = [el for el in cur]

        return temp

    @staticmethod
    def get_avg_salary(cur):

        cur.execute("""
                select avg(salary)
                from vacancies;
                """)
        temp = [el for el in cur]

        # Закрытие коннекта

        return temp[0][0]

    @staticmethod
    def get_vacancies_with_higher_salary(cur):
        cur.execute(f"select * from vacancies where salary > {DBManager.get_avg_salary(cur)}")
        temp = [el for el in cur]

        # Закрытие коннекта

        return temp

    @staticmethod
    def get_vacancies_with_keyword(user_input, cur):
        cur.execute(f"select * from vacancies where vacancies.name like '%{user_input}%'")
        temp = [el for el in cur]

        # Закрытие коннекта

        return temp
