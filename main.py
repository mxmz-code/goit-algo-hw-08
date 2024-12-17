import heapq
import random
import os
import logging
from colorama import Fore, Back, Style, init
from heapq import merge

# Ініціалізація colorama
init(autoreset=True)

# Налаштування логування
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Функція для генерації випадкових довжин кабелів
def generate_random_lengths(n, min_len=1, max_len=100):
    """
    Генерує список випадкових довжин кабелів.

    Параметри:
    n (int): Кількість кабелів.
    min_len (int): Мінімальна довжина кабелю.
    max_len (int): Максимальна довжина кабелю.

    Повертає:
    list: Список випадкових довжин кабелів.
    """
    lengths = random.choices(range(min_len, max_len + 1), k=n)
    logging.info(f"Згенеровані довжини кабелів: {lengths}")
    return lengths

# Функція для обчислення мінімальних витрат на з'єднання кабелів
def connect_two_smallest(cables):
    """
    З'єднує два найменших кабелі та повертає вартість цього з'єднання.

    Параметри:
    cables (list): Черга з мінімальним пріоритетом для довжин кабелів.

    Повертає:
    int: Вартість з'єднання.
    """
    first = heapq.heappop(cables)
    second = heapq.heappop(cables)
    cost = first + second
    heapq.heappush(cables, cost)
    logging.info(f"З'єднано кабелі з витратами: {cost}")
    return cost

def connect_cables(cables):
    """
    Виконує з'єднання кабелів з мінімальними загальними витратами.

    Параметри:
    cables (list): Список довжин кабелів.

    Повертає:
    int: Загальні витрати.
    """
    if not cables:
        print(Fore.RED + "Список кабелів не може бути порожнім!")
        logging.error("Список кабелів порожній!")
        return

    if len(cables) == 1:
        print(Fore.YELLOW + "Тільки один кабель. Витрати відсутні.")
        logging.info("Тільки один кабель. Витрати відсутні.")
        return 0

    heapq.heapify(cables)
    total_cost = 0
    step = 1

    print(Fore.YELLOW + "\nПроцес з'єднання кабелів (мінімізація загальних витрат):")

    while len(cables) > 1:
        cost = connect_two_smallest(cables)
        total_cost += cost
        print(Fore.GREEN + f"Крок {step}: з'єднано кабелі з витратами {cost}.")
        logging.info(f"Крок {step}: з'єднано кабелі з витратами {cost}.")
        step += 1

    return total_cost

# Функція для злиття кількох відсортованих списків в один відсортований список
def merge_k_lists(lists):
    """
    Зливає кілька відсортованих списків в один.

    Параметри:
    lists (list of list): Список відсортованих списків.

    Повертає:
    list: Злитий відсортований список.
    """
    merged = list(merge(*lists))
    logging.info(f"Злитий відсортований список: {merged}")
    return merged

# Функція для очищення екрану
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Функція для красивого текстового виводу
def print_header():
    print(Fore.MAGENTA + Style.BRIGHT + "+" + "-"*48 + "+")
    print(Fore.MAGENTA + Style.BRIGHT + "|{:^48}|".format("Завдання з'єднання мережевих кабелів"))
    print(Fore.MAGENTA + Style.BRIGHT + "+" + "-"*48 + "+")

# Функція для отримання кількості кабелів
def get_number_of_cables():
    while True:
        try:
            n = int(input(Fore.YELLOW + "Введи кількість кабелів (мінімум 2): "))
            if n < 2:
                print(Fore.RED + "Кількість кабелів повинна бути більше або рівна 2.")
                logging.warning("Користувач ввів неправильну кількість кабелів.")
                continue
            return n
        except ValueError:
            print(Fore.RED + "Введи коректне числове значення!")
            logging.warning("Користувач ввів некоректне значення.")

# Функція для отримання довжин кабелів вручну
def get_cable_lengths(n):
    cables = []
    for i in range(n):
        while True:
            try:
                length = int(input(Fore.YELLOW + f"Довжина кабелю {i + 1}: "))
                if length <= 0:
                    print(Fore.RED + "Довжина кабелю повинна бути додатнім числом!")
                    logging.warning(f"Користувач ввів некоректну довжину кабелю {length}.")
                    continue
                cables.append(length)
                break
            except ValueError:
                print(Fore.RED + "Введи коректне числове значення!")
                logging.warning("Користувач ввів некоректне значення для довжини кабелю.")
    return cables

# Генерація випадкових відсортованих списків
def generate_sorted_lists(k, min_len=3, max_len=10, min_value=1, max_value=20):
    """
    Генерує випадкові відсортовані списки.

    Параметри:
    k (int): Кількість списків.
    min_len (int): Мінімальна довжина кожного списку.
    max_len (int): Максимальна довжина кожного списку.
    min_value (int): Мінімальне значення в списку.
    max_value (int): Максимальне значення в списку.

    Повертає:
    list of list: Список відсортованих списків.
    """
    lists = []
    for _ in range(k):
        length = random.randint(min_len, max_len)
        list_data = sorted(random.randint(min_value, max_value) for _ in range(length))
        lists.append(list_data)
    logging.info(f"Згенеровані відсортовані списки: {lists}")
    return lists

# Функція для отримання відсортованих списків вручну
def get_sorted_lists():
    while True:
        try:
            k = int(input(Fore.YELLOW + "Введи кількість відсортованих списків (мінімум 1): "))
            if k < 1:
                print(Fore.RED + "Кількість списків повинна бути не менше 1!")
                logging.warning("Користувач ввів неправильну кількість списків.")
                continue
            break
        except ValueError:
            print(Fore.RED + "Введи коректне числове значення!")
            logging.warning("Користувач ввів некоректне значення для кількості списків.")
    
    lists = []
    for i in range(k):
        while True:
            print(Fore.GREEN + f"Введи відсортований список {i + 1}:")
            user_input = input(Fore.YELLOW + "Введи елементи списку через пробіл: ")
            try:
                lst = list(map(int, user_input.split()))
                if lst != sorted(lst):
                    print(Fore.RED + "Список не відсортований! Спробуйте ще раз.")
                    logging.warning(f"Користувач ввів не відсортований список: {lst}")
                    continue
                if len(lst) == 0:
                    print(Fore.RED + "Список не може бути порожнім! Спробуйте ще раз.")
                    logging.warning("Користувач ввів порожній список.")
                    continue
                lists.append(lst)
                break
            except ValueError:
                print(Fore.RED + "Будь ласка, введіть тільки числа через пробіл!")
                logging.warning("Користувач ввів некоректні значення для елементів списку.")
    return lists

# Функція для отримання кількості відсортованих списків
def get_number_of_sorted_lists():
    while True:
        try:
            k = int(input(Fore.YELLOW + "Введи кількість відсортованих списків: "))
            if k < 1:
                print(Fore.RED + "Кількість списків повинна бути не менше 1!")
                logging.warning("Користувач ввів неправильну кількість списків.")
                continue
            return k
        except ValueError:
            print(Fore.RED + "Введи коректне числове значення!")
            logging.warning("Користувач ввів некоректне значення для кількості списків.")

# Основний діалог з користувачем
def main():
    while True:
        clear_screen()
        print_header()

        print(Fore.BLUE + "\nПривіт! Це завдання по з'єднанню мережевих кабелів.")
        print(Fore.GREEN + "Вибери один з варіантів:")
        print(Fore.YELLOW + "1. Об'єднання мережевих кабелів")
        print(Fore.YELLOW + "2. Сортування за допомогою merge_k_lists")
        print(Fore.RED + "3. Вихід з програми")

        choice = input(Fore.YELLOW + "Вибір: ").strip()

        if choice == '1':
            print(Fore.GREEN + "Вибери спосіб введення даних:")
            print(Fore.YELLOW + "1. Ввести довжини кабелів вручну")
            print(Fore.YELLOW + "2. Автоматично згенерувати довжини кабелів")
            sub_choice = input(Fore.YELLOW + "Вибір: ").strip()

            if sub_choice == '1':
                n = get_number_of_cables()
                cables = get_cable_lengths(n)
            elif sub_choice == '2':
                n = get_number_of_cables()
                cables = generate_random_lengths(n)
                print(Fore.GREEN + "Згенеровані довжини кабелів:", cables)
            else:
                print(Fore.RED + "Невірний вибір! Спробуйте ще раз.")
                continue

            total_cost = connect_cables(cables)
            if total_cost is not None:
                print(Fore.MAGENTA + "\nПроцес завершено!")
                print(Fore.YELLOW + f"Мінімальні загальні витрати на з'єднання кабелів: {total_cost}")
            input(Fore.YELLOW + "\nНатисни Enter для повернення в головне меню...")

        elif choice == '2':
            print(Fore.GREEN + "Вибери спосіб введення даних:")
            print(Fore.YELLOW + "1. Ввести відсортовані списки вручну")
            print(Fore.YELLOW + "2. Автоматично згенерувати відсортовані списки")
            sub_choice = input(Fore.YELLOW + "Вибір: ").strip()

            if sub_choice == '1':
                lists = get_sorted_lists()
            elif sub_choice == '2':
                k = get_number_of_sorted_lists()  # Використовуємо нову функцію
                lists = generate_sorted_lists(k)
                print(Fore.GREEN + "Згенеровані відсортовані списки:", lists)
            else:
                print(Fore.RED + "Невірний вибір! Спробуйте ще раз.")
                continue

            merged_list = merge_k_lists(lists)
            print(Fore.MAGENTA + "\nРезультат злиття відсортованих списків:")
            print(Fore.YELLOW + f"Злитий відсортований список: {merged_list}")
            input(Fore.YELLOW + "\nНатисни Enter для повернення в головне меню...")

        elif choice == '3':
            print(Fore.CYAN + "Дякуємо за використання програми! До зустрічі.")
            logging.info("Програма завершена.")
            break
        else:
            print(Fore.RED + "Невірний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main()
