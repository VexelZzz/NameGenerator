import random

first_names = ["Эйдриан", "Алистер", "Амара", "Ансель", "Арден", "Беатрис", "Селест", "Дориан", "Элиас", "Эллоуэн", "Эвандер", "Феликс", "Фрейя", "Гидеон", "Айрис", "Джулиан", "Леона", "Люциан", "Мейв", "Нолан", "Одесса", "Сайлас", "Талия", "Тристан"]
last_names = ["Эшфорд", "Беллами", "Блэквуд", "Колдуэлл", "Карвер", "Кавано", "Кросс", "Эллери", "Фэйрчайлд", "Флетчер", "Грейвс", "Харлоу", "Хоторн", "Мерсер", "Найтингейл", "Норт", "Прескотт", "Куинн", "Стерлинг", "Вейл", "Уитакер", "Рен", "Олдридж", "Боумонт"]

generated_names = set()
count = 0
max_names = len(first_names) * len(last_names)

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

def generate_names():
    while len(generated_names) < count:
        full_name = random.choice(first_names) + " " + random.choice(last_names)
        if full_name not in generated_names:
            generated_names.add(full_name)
    return generated_names

generate_names()
for number, name in enumerate(generated_names, start=1):
    print(f"{number}. {name}")








