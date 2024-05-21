# # def shaker_sort(values):
# #     if not values:
# #         return
# #     left = 0
# #     right = len(values) - 1
# #     while left <= right:
# #         for i in range(right, left, -1):
# #             if values[i - 1] > values[i]:
# #                 values[i - 1], values[i] = values[i], values[i - 1]
# #         left += 1
# #         for i in range(left, right):
# #             if values[i] > values[i + 1]:
# #                 values[i], values[i + 1] = values[i + 1], values[i]
# #         right -= 1


# # if __name__ == "__main__":
# #     values = [5, 2, 9, 11, 5, 6]
# #     print("Before sorting:", values)
# #     shaker_sort(values)
# #     print("After sorting:", values)


# # def merge_sort_impl(values, buffer, l, r):
# #     if l < r:
# #         m = (l + r) // 2
# #         merge_sort_impl(values, buffer, l, m)
# #         merge_sort_impl(values, buffer, m + 1, r)

# #         k = l
# #         i, j = l, m + 1
# #         while i <= m or j <= r:
# #             if j > r or (i <= m and values[i] < values[j]):
# #                 buffer[k] = values[i]
# #                 i += 1
# #             else:
# #                 buffer[k] = values[j]
# #                 j += 1
# #             k += 1

# #         for i in range(l, r + 1):
# #             values[i] = buffer[i]


# # def merge_sort(values):
# #     if values:
# #         buffer = [0] * len(values)
# #         merge_sort_impl(values, buffer, 0, len(values) - 1)

# # # Пример использования функции
# # if __name__ == "__main__":
# #     values = [5, 2, 9, 1, 5, 6]
# #     print("Before sorting:", values)
# #     merge_sort(values)
# #     print("After sorting:", values)

# # def partition(values, l, r):
# #     x = values[r]
# #     less = l

# #     for i in range(l, r):
# #         if values[i] <= x:
# #             values[i], values[less] = values[less], values[i]
# #             less += 1

# #     values[less], values[r] = values[r], values[less]     
# #     return less

# # def quick_sort_impl(values, l, r):
# #     if l < r:
# #         q = partition(values, l, r)
# #         quick_sort_impl(values, l, q - 1)
# #         quick_sort_impl(values, q + 1, r)

# # def quick_sort(values):
# #     if values:
# #         quick_sort_impl(values, 0, len(values) - 1)

# # # быстрая сортировка
# # if __name__ == "__main__":
# #     values = [5, 2, 9, 1,  6]
# #     print("Before sorting:", values)
# #     quick_sort(values)
# # #     print("After sorting:", values)

# # class Solution:
# #     def longestCommonPrefix(self,strs: list[str])->str:
# #         pref = strs[0]
# #         pref_len = len(pref)
# #         for s in strs[1:]:
# #             while pref != s[0:pref_len]:
# #                 pref_len -= 1
# #                 if pref_len == 0:
# #                     return ''
# #                 pref = pref[0:pref_len]
# #             return pref
        
# # # main = 'hello'
# # from datetime import datetime

# # def add_visitor(file_path):
# #     with open(file_path, 'a') as file:
# #         while True:
# #             name = input("Введите имя: ")
# #             surname = input("Введите фамилию: ")
# #             phone = input("Введите номер телефона: ")

# #             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# #             file.seek(0, 2)  
# #             if file.tell() == 0:
# #                 next_id = 1
# #                 file.write("ID,Name,Surname,Phone,Timestamp\n")  
# #             else:
# #                 file.seek(0)  
# #                 lines = file.readlines()
# #                 last_line = lines[-1]
# #                 last_id = int(last_line.split(',')[0])
# #                 next_id = last_id + 1

# #             file.write(f"{next_id},{name},{surname},{phone},{timestamp}\n")
# #             print(f"Посетитель {name} {surname} успешно добавлен в журнал.\n")

# #             cont = input("Хотите добавить еще одного посетителя? (да/нет): ").strip().lower()
# #             if cont != 'да':
# #                 break

# # if __name__ == "__main__":
# #     journal_file = "journal.csv"
# #     add_visitor(journal_file)
# def process_students(file_path):
#     students = []
#     total_score = 0
#     count = 0

#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             name, score = line.rsplit(' ', 1)
#             score = int(score)
#             students.append((name, score))
#             total_score += score
#             count += 1

#     print("Учащиеся с оценкой меньше 3 баллов:")
#     for student in students:
#         if student[1] < 3:
#             print(student[0])
    
#     average_score = total_score / count
#     print(f"\nСредний балл по классу: {average_score:.2f}")

# if __name__ == "__main__":
#     file_path = "students.txt"
#     process_students(file_path)




# def get_office_files():
#     return {
#         1: "google_kazakstan.txt",
#         2: "google_paris.txt",
#         3: "google_uar.txt",
#         4: "google_kyrgystan.txt",
#         5: "google_san_francisco.txt",
#         6: "google_germany.txt",
#         7: "google_moscow.txt",
#         8: "google_sweden.txt"
#     }

# def print_office_choices(office_files):
#     print("Пожалуйста, выберите офис для отправки жалобы:")
#     for number, filename in office_files.items():
#         print(f"{number}. {filename.split('_')[1].capitalize()}")

# def main():
#     greeting = input("Введите 'Привет' для начала: ").strip().lower()
#     if greeting == "привет":
#         office_files = get_office_files()
#         print_office_choices(office_files)
        
#         try:
#             choice = int(input("Введите номер офиса: "))
#             if choice in office_files:
#                 complaint = input("Введите вашу жалобу: ").strip()
#                 with open(office_files[choice], 'a', encoding='utf-8') as file:
#                     file.write(complaint + "\n")
#                 print(f"Ваша жалоба была записана в {office_files[choice]}")
#             else:
#                 print("Неверный выбор офиса. Пожалуйста, попробуйте снова.")
#         except ValueError:
#             print("Пожалуйста, введите числовое значение.")
#     else:
#         print("Вы не ввели 'Привет'. Программа завершена.")

# if __name__ == "__main__":
#     main()

# forbidden_words = ['world', 'color', 'twitter', 'putin', 'book']

# with open('forbidden_words.txt', 'w') as file:
#     for word in forbidden_words:
#         file.write(word + '\n')

# def censor_string(input_string):
#     with open('forbidden_words.txt', 'r') as file:
#         forbidden_words = [line.strip() for line in file]

#     for word in forbidden_words:
#         input_string = input_string.replace(word, '*' * len(word))

#     return input_string

# input_string = input("Введите строку: ")
# output_string = censor_string(input_string)
# print("Вывод:", output_string)
#первая
def calculate_total(data, product_numbers):
    total_sum = 0

    for number in product_numbers:
        if number in data:
            total_sum += data[number]["price"]

    return total_sum

data = {
    "20": {"name": "Джинсы Ricardo", "price": 1500},
    "23": {"name": "Кепка Balenciaga", "price": 890},
    "41": {"name": "Iphone 13 Pro Max", "price": 95000},
    "55": {"name": "Кофта Теплая", "price": 2500},
    "12": {"name": "Футболка Nike", "price": 500},
    "71": {"name": "Крассовки Nike", "price": 2200},
}

user_input = input("Введите номера товаров через пробел: ").strip()
product_numbers = user_input.split()

total_sum = calculate_total(data, product_numbers)
print(f"Общая сумма: {total_sum} сом")
#вторая
  
data = {
    "куринное яйцо": 157,
    "крупа манная": 333,
    "хлеб": 235,
    "чечевица": 295,
    "арахис": 552,
    "миндаль": 609,
    "капуста": 28,
    "виноград": 72,
    "персик": 45,
    "молоко": 60,
}

def calculate_calories(data, product_name, weight):
    if product_name in data:
        calories_per_100g = data[product_name]
        total_calories = (calories_per_100g * weight) / 100
        return total_calories
    else:
        return None

user_input = input("Введите название продукта и его количество в граммах (например, арахис-500): ").strip()
try:
    product_name, weight = user_input.split('-')
    weight = int(weight.strip())
    product_name = product_name.strip().lower()

    total_calories = calculate_calories(data, product_name, weight)

    if total_calories is not None:
        print(f"Калорийность {product_name} - {total_calories:.2f} Ккал")
    else:
        print(f"Продукт '{product_name}' не найден в базе данных.")
except ValueError:
    print("Неверный формат ввода. Пожалуйста, введите данные в формате 'продукт-количество'.")

        
        
#четвертая
def add_word(en_ru_words):
    english_word = input("Введите английское слово: ").strip().lower()
    russian_translation = input("Введите его русский перевод: ").strip().lower()
    en_ru_words[english_word] = russian_translation
    print(f"Слово '{english_word}' с переводом '{russian_translation}' добавлено в словарь.")

def get_translation(en_ru_words):
    english_word = input("Введите английское слово для перевода: ").strip().lower()
    translation = en_ru_words.get(english_word)
    if translation:
        print(f"Перевод слова '{english_word}' - '{translation}'.")
    else:
        print(f"Слово '{english_word}' не найдено в словаре.")

def main():
    en_ru_words = {
        "apple": "яблоко",
        "banana": "банан",
        "orange": "апельсин"
    }

    while True:
        print("\nВыберите команду:")
        print("1) Добавить слово и перевод")
        print("2) Получить перевод слова")
        print("3) Выйти")
        
        command = input("Введите номер команды: ").strip()
        
        if command == "1":
            add_word(en_ru_words)
        elif command == "2":
            get_translation(en_ru_words)
        elif command == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверная команда. Пожалуйста, введите 1, 2 или 3.")

main()

#пятая
import random


secret_number = random.randint(1, 100)

print("Я загадал число от 1 до 100. Попробуй угадать его!")


while True:
    try:
        # Ввод числа пользователем
        guess = int(input("Введите ваше число: "))
        
        if guess < 1 or guess > 100:
            print("Пожалуйста, введите число в диапазоне от 1 до 100.")
            continue

        if guess < secret_number:
            print("Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print("Поздравляю! Вы угадали число.")
            break
    except ValueError:
        print("Пожалуйста, введите корректное число.")

print("Игра окончена.")
#шестая
candidates = {}

def vote_for_candidate(candidates, candidate_name):

    if candidate_name in candidates:
        candidates[candidate_name] += 1
    else:
        candidates[candidate_name] = 1

def show_results(candidates):
    if not candidates:
        print("Голосов еще нет.")
    else:
        for candidate, votes in candidates.items():
            print(f"{candidate}: {votes} голосов")

print("Добро пожаловать на избирательный учет!")

while True:
    print("\n1. Проголосовать за кандидата")
    print("2. Посмотреть текущие результаты")
    print("3. Выйти")
    try:
        action = int(input("Выберите действие: ").strip())
        
        if action == 1:
            candidate_name = input("Введите имя кандидата: ").strip()
            vote_for_candidate(candidates, candidate_name)
            print(f"Ваш голос за {candidate_name} учтен.")
        
        elif action == 2:
            show_results(candidates)
        
        elif action == 3:
            print("Выход из программы.")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")
    
    except ValueError:
        print("Пожалуйста, введите числовое значение.")
emails = {
    'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
    'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
    'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
    'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
    'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
    'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']
}

def add_email(email):
    username, domain = email.split('@')
    
    if domain in emails:
        emails[domain].append(username)
    else:
        emails[domain] = [username]


user_email = input("Введите email: ")


add_email(user_email)


print(emails)
#десятая
def max_money(houses):
    if not houses:
        return 0
    
    
    if len(houses) == 1:
        return houses[0]
    
    max_money_at_house = [0] * len(houses)
    
    
    max_money_at_house[0] = houses[0]
    max_money_at_house[1] = max(houses[0], houses[1])
    
    
    for i in range(2, len(houses)):
        max_money_at_house[i] = max(max_money_at_house[i-1], max_money_at_house[i-2] + houses[i])
    
    
    return max_money_at_house[-1]


houses = [5, 4, 2, 8]
print(max_money(houses))  
#одиннадцатая задача
def check_words(word1, word2):
    
    if len(word1) != len(word2):
        return False
    
    
    return sorted(word1) == sorted(word2)


print(check_words('логика', 'иголка'))  
print(check_words('кот', 'тор'))        
#двенадцатая
def is_perfect_number(number):
    divisors_sum = 0
    
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            divisors_sum += i
    
    return divisors_sum == number


print(is_perfect_number(28))   
print(is_perfect_number(12))   
#тринадцатая
import re

def sum_of_integers_in_string(s):
    numbers = re.findall(r'\d+', s)
    
    
    total_sum = sum(int(num) for num in numbers)
    
    return total_sum

# Пример использования
s = "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"
print(sum_of_integers_in_string(s))  # Выведет 3635
#четырнадцатая
def number_to_russian_word(number):
    russian_words = {
        0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
        5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
        10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
        14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать',
        18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
        40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
        80: 'восемьдесят', 90: 'девяносто', 100: 'сто', 200: 'двести',
        300: 'триста', 400: 'четыреста', 500: 'пятьсот', 600: 'шестьсот',
        700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот'
    }
    
    
    if number in russian_words:
        return russian_words[number]
    
    
    digits = [int(d) for d in str(number)]
    length = len(digits)
    

    word = ''
    for i, digit in enumerate(digits):
        if (length - i) % 3 == 2:  
            if digit == 1:
                word += russian_words[digit * 10 + digits[i+1]]
                break
            else:
                word += russian_words[digit * 10]
        elif (length - i) % 3 == 1:  
            if digit != 0:
                word += russian_words[digit]
                if i < length - 1:
                    word += ' '
        elif (length - i) % 3 == 0:  
            if digit != 0:
                word += russian_words[digit * 100]
                if i < length - 1:
                    word += ' '
    
    return word

def sort_numbers_by_russian_name_length(numbers):
    
    def russian_name_length(num):
        return len(number_to_russian_word(num))
    
    
    
    sorted_numbers = sorted(numbers, key=lambda x: (russian_name_length(x), x))
    
    return sorted_numbers


numbers = [1, 9, 3, 10, 2]
sorted_numbers = sort_numbers_by_russian_name_length(numbers)
print(sorted_numbers)  

#пятнадцатая
def get_max_len(s):
    
    start = 0
    end = 0
    max_length = 0
    window = set()
    
    
    while end < len(s):
        if s[end] in window:
            window.remove(s[start])
            start += 1
        else:
            window.add(s[end])
            end += 1
            max_length = max(max_length, end - start)
    
    return max_length


print(get_max_len("abcdadba"))  
print(get_max_len("qwerty"))     
