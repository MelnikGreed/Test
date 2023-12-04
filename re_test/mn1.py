import pytest

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


# Добавьте сюда ваш код из Задачи 1
all_list = []
for m in mentors:
	# Допишите здесь ваш код, который заполнит all_list. Можете как складывать списки, так и использовать метод extend
     all_list = mentors[0] + mentors[1] + mentors[2] + mentors[3]
# Сделайте список all_names_list, состоящий только из имён, и заполните его
all_names_list = []
for mentor in all_list:
	name = mentor.split()[0]
	all_names_list.append(name)
# Уникальные имена будут в unique_names
unique_names = all_names_list

# Подсчитайте встречаемость каждого имени через list.count()
popular = []
for name in all_names_list:
    popular.append((name, all_names_list.count(name))) # добавьте подсчет имен

    popular = list(set(popular))

popular.sort(key=lambda x:x[1], reverse=True)

# Получите топ-3 часто встречающихся имён из списка popular
# Подсказка: возьмите срез списка
top_3 = popular[0:3]
top= [f"{str(i[0])}: {str(i[1])} раз(а)" for i in top_3]
print(", ".join(top))

def test_all_list():
    assert all_list == ['Евгений Шмаргунов', 'Олег Булыгин', 'Дмитрий Демидов', 'Кирилл Табельский', 'Александр Ульянцев', 'Александр Бардин', 'Александр Иванов', 'Антон Солонилин', 'Максим Филипенко', 'Елена Никитина', 'Азамат Искаков', 'Роман Гордиенко', 'Филипп Воронов', 'Анна Юшина', 'Иван Бочаров', 'Анатолий Корсаков', 'Юрий Пеньков', 'Илья Сухачев', 'Иван Маркитан', 'Ринат Бибиков', 'Вадим Ерошевичев', 'Тимур Сейсембаев', 'Максим Батырев', 'Никита Шумский', 'Алексей Степанов', 'Денис Коротков', 'Антон Глушков', 'Сергей Индюков', 'Максим Воронцов', 'Евгений Грязнов', 'Константин Виролайнен', 'Сергей Сердюк', 'Павел Дерендяев', 'Евгений Шмаргунов', 'Олег Булыгин', 'Александр Бардин', 'Александр Иванов', 'Кирилл Табельский', 'Александр Ульянцев', 'Роман Гордиенко', 'Адилет Асканжоев', 'Александр Шлейко', 'Алена Батицкая', 'Денис Ежков', 'Владимир Чебукин', 'Эдгар Нуруллин', 'Евгений Шек', 'Максим Филипенко', 'Елена Никитина', 'Владимир Чебукин', 'Эдгар Нуруллин', 'Евгений Шек', 'Валерий Хаслер', 'Татьяна Тен', 'Александр Фитискин', 'Александр Шлейко', 'Алена Батицкая', 'Александр Беспоясов', 'Денис Ежков', 'Николай Лопин', 'Михаил Ларченко']
def test_all_names_list():
    assert all_names_list == ['Евгений', 'Олег', 'Дмитрий', 'Кирилл', 'Александр', 'Александр', 'Александр', 'Антон', 'Максим', 'Елена', 'Азамат', 'Роман', 'Филипп', 'Анна', 'Иван', 'Анатолий', 'Юрий', 'Илья', 'Иван', 'Ринат', 'Вадим', 'Тимур', 'Максим', 'Никита', 'Алексей', 'Денис', 'Антон', 'Сергей', 'Максим', 'Евгений', 'Константин', 'Сергей', 'Павел', 'Евгений', 'Олег', 'Александр', 'Александр', 'Кирилл', 'Александр', 'Роман', 'Адилет', 'Александр', 'Алена', 'Денис', 'Владимир', 'Эдгар', 'Евгений', 'Максим', 'Елена', 'Владимир', 'Эдгар', 'Евгений', 'Валерий', 'Татьяна', 'Александр', 'Александр', 'Алена', 'Александр', 'Денис', 'Николай', 'Михаил']
def test_top_3():
    assert top_3 == [("Александр", 10), ("Евгений", 5), ("Максим", 4)]
