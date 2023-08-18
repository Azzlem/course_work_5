from csv.employeers import Employers
from csv.vacancies import Vacancies
from csv.utils import drop_table, LaconicOutputToUser

print("Please Wait")
Employers.make_table()
Vacancies.make_table()
print("Bases successfully makes")

while True:
    print(f"Нажмите 1 если вы хотите получить список всех компаний и количество вакансий у них.\n"
          f"Нажмите 2 если вы хотите получить список всех вакансий. \n"
          f"Нажмите 3 если вы хотите получить среднюю зарплату по вакансиям.\n"
          f"Нажмите 4 если вы хотите получить список вакансий у которых зарплата выше средней\n"
          f"Нажмите 5 если вы хотите получить список вакансий отфильтрованный по вашему ключевому слову\n"
          f"Введите exit если вам больше ничего не надо.\n")
    user_input = input("Ваш ввод: ")
    if user_input == "1":
        print(LaconicOutputToUser.laconic_companies_and_vacancies_count())
    elif user_input == "2":
        print(LaconicOutputToUser.laconic_all_vacancies())
    elif user_input == "3":
        print(LaconicOutputToUser.laconic_avg())
    elif user_input == "4":
        print(LaconicOutputToUser.laconic_vacancies_with_higher_salary())
    elif user_input == "5":
        print(LaconicOutputToUser.laconic_get_vacancies_with_keyword())
    elif user_input == "exit":
        print("Хорошего дня. До свидания.")
        break
    else:
        print("Что то пошло не так, введите ещё раз ваш выбор.")


drop_table()
