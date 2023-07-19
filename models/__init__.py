# import sqlite3 as sq
#
# def read_avatar(filename):
#     try:
#         with open(f'avatars/{filename}', 'rb') as file:
#             return file.read()
#     except IOError as e:
#         print(e)
#         return None
#
# def write_avatar(filepath, data):
#     try:
#         with open(filepath, 'wb') as file:
#             file.write(data)
#             return True
#     except IOError as e:
#         print(e)
#         return False
#
# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     # cur.execute('''SELECT * FROM cars''')
#     # for car in cur:
#     #     print(car['model'], car['price'])
#
#     cur.execute('''CREATE TABLE IF NOT EXISTS users(
#                     user_id INTEGER PRIMARY KEY,
#                     avatar BLOB,
#                     name TEXT
#                     )''')

    # img = read_avatar('1.png')
    # sqlite_img = sq.Binary(img)
    # cur.execute('''INSERT INTO users VALUES (1, ?, ?)''', (sqlite_img, 'Василий'))

    # cur.execute('''SELECT avatar FROM users''')
    # img = cur.fetchone()[0]
    # write_avatar('avatars/new.png', img)


    # with open('cars_backup.sql', 'w') as f:
    #     for i in con.iterdump():
    #         f.write(f'{i}\n')

    # sql_script = open('cars_backup.sql')
    # cur.execute('sql_script')

# with sq.connect(':memory:') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS users(
#                         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         avatar BLOB,
#                         name TEXT
#                         )''')
#
#     cur.executemany('''INSERT INTO users VALUES(NULL, ?, ?)''',
#                     [(i, i**2) for i in range(10000)])
#     cur.execute('SELECT * FROM users')
#     print(cur.fetchall())
#     input()

# import os
#
# from  sqlalchemy import and_, or_, not_, desc, func, text
# from models.database import DATABASE_NAME, Session
# import create_database as db_creator
#
# from models.groups import Group
# from models.lessons import Lesson, association_table
# from models.students import Student

# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
#
#     session = Session()
    # print(session.query(Lesson).all())
    # for lesson in session.query(Lesson).all():
    #     print(lesson.lesson_title, lesson.groups)

    # for group in session.query(Group).all():
    #     print(group.group_name, group.lessons)

    # print(session.query(Lesson).get(3)) устаревший
    # print(session.get(Lesson, 3))

    # for lesson in session.query(Lesson.lesson_title).filter(or_(Lesson.id < 3, Lesson.lesson_title.like('Ф%'))):
    #     print(lesson)

    # for lesson, gr in session.query(Lesson.lesson_title, Group.group_name).filter(
    #         association_table.c.lesson_id == Lesson.id,
    #         association_table.c.group_id == Group.id,
    # ):
    #     print(lesson, gr)

    # print(session.query(Lesson).filter(Lesson.id.in_([1, 2, 3])).all())
    # print(session.query(Lesson).filter(Lesson.id.notin_([1, 2, 3])).all())

    # print(session.query(Student).filter(not_(Student.age.between(18, 20))).all())

    # print(session.query(Student).filter(Student.age.like('2%')).all())

    # print(session.query(Student).filter(Student.age.like('2%')).limit(4).all())
    # print(session.query(Student).filter(Student.age.like('2%')).limit(4).offset(2).all())


    # for student in session.query(Student).filter(Student.age.like('1%')).order_by(desc(Student.surname)).all():
    #     print(student)

    # print(session.query(Student, Group).join(Group))
    # for it in session.query(Student, Group).join(Group).filter(Group.group_name == 'Слизерин'):
    #     print(it)

    # for it in session.query(Group.group_name, func.count(Student.id)).join(Group).group_by(Group.id).having(func.count(Student.id) > 25):
    #     print(it)

    # for it in session.query(Student).filter(text('surname LIKE "М%" ')):
    #     print(it)



# Урок от 09.07.2023
# from jinja2 import Template
#
# person = {
#     'name': 'Иван',
#     'age': 20
# }
# # age = 20
#
# tm = Template('Меня зовут {{ p.name }}. Мне {{ p["age"] }} лет')
# msg = tm.render(p=person)
# print(msg)




# from jinja2 import Template
#
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
# person = Person('Иван', 20)
# tm = Template('Меня зовут {{ p.name }}. Мне {{ p.get_age() }} лет')
# msg = tm.render(p=person)
# print(msg)


# from jinja2 import Template
#
# data = '''{% raw %}Модуль Jinja вместо определения {{ name }}
# подставит соответствующее значениею. {% endraw %}'''
#
# tm = Template(data)
# msg = tm.render()
# print(msg)


# from jinja2 import Template
#
# link = '''In HTML-document link would look like this
# <a href="#">Link</a>'''
#
# tm = Template('{{ link | e }}')
# msg = tm.render(link=link)
# print(msg)


# from jinja2 import Template
# # Циклы for и условия if elif else
# cities = [
#     {'id': 1, 'name': 'Москва'},
#     {'id': 2, 'name': 'Сочи'},
#     {'id': 3, 'name': 'Санкт-Петербург'},
#     {'id': 4, 'name': 'Новосибирск'},
# ]
#
# data = """
# {% for city in cities -%}
#     {% if city.id > 2 -%}
#         <p>{{ city.id }} {{ city.name }}</p>
#     {% elif city.name == 'Москва' -%}
#         <h1>{{ city.name }}</h1>
#     {% endif %}
# {% endfor %}
# """
# tm = Template(data)
# msg =tm.render(cities=cities)
# print(msg)


from jinja2 import Template
menu = [
    {'url': 'index', 'name': 'Главная'},
    {'url': 'news', 'name': 'Новости'},
    {'url': 'about', 'name': 'О компании'},
    {'url': 'shop', 'name': 'Магазин'},
    {'url': 'contacts', 'name': 'Контакты'},
]

tm = Template('''
<ul>
{% for el in menu -%}
    <li><a href="/{{ el.url }}" class="active"> {{ el.name }}</a></li>
    {% else %}
    <li><a href="/{{ el.url }}">{{ el.name }}</a></li>
    {% endfor %}
</ul>  
''')

msg =tm.render(menu=menu)
print(msg)