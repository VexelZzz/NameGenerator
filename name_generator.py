import random

# Список имён и фамилий
first_names = ["Эйдриан", "Алистер", "Амара", "Ансель", "Арден", "Беатрис", "Селест", "Дориан", "Элиас", "Эллоуэн", "Эвандер", "Феликс", "Фрейя", "Гидеон", "Айрис", "Джулиан", "Леона", "Люциан", "Мейв", "Нолан", "Одесса", "Сайлас", "Талия", "Тристан"]
last_names = ["Эшфорд", "Беллами", "Блэквуд", "Колдуэлл", "Карвер", "Кавано", "Кросс", "Эллери", "Фэйрчайлд", "Флетчер", "Грейвс", "Харлоу", "Хоторн", "Мерсер", "Найтингейл", "Норт", "Прескотт", "Куинн", "Стерлинг", "Вейл", "Уитакер", "Рен", "Олдридж", "Боумонт"]

count = 0
max_names = len(first_names) * len(last_names) # Лимит возможных комбинаций

# Цикл с проверками исключений
while count <= 0 or count > max_names:
    try:
        count = int(input("Сколько имён сгенерировать? "))
    except ValueError:
        print("Нужно ввести целое число!")
        continue
    if count <= 0:
        print("Нужно ввести положительное число!")
        continue
    elif count > max_names:
        print(f"Вы не можете ввести число больше, чем {max_names}")
        continue

# Создание полных имён
def generate_names(count, first_names, last_names):
    if count > len(first_names) * len(last_names):
        raise ValueError("Запрошено больше имён, чем существует уникальных комбинаций!")
    generated_names = set()
    while len(generated_names) < count:
        full_name = random.choice(first_names) + " " + random.choice(last_names)
        if full_name not in generated_names:
            generated_names.add(full_name)
    return generated_names

def show_count(count):
    print(f"Будет сгенерировано {count} имён")

# Вывод имён построчно
generated_names = generate_names(count, first_names, last_names)
show_count(count)
for number, name in enumerate(generated_names, start=1):
    print(f"{number}. {name}")








