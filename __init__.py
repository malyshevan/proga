import sys

from url_programma import storage

get_connection = lambda: storage.connect ('base.sqlite')

#def find_all(conn):
#    with conn:
#        c = conn.execute(SQL_SELECT_ALL)
#        return c.fetchall()


def list_task():
    with get_connection() as conn:
        task = storage.find_all(conn)
    print (task)


def add_task():
    task = input('\nВведите новую задачу: ')
    status = input('\nВведите статус задачи: ')
    with get_connection() as conn:
        storage.add_task(conn, task, status)
    print('\nЗадача добавлена!')


def edit_task():
    id = input ('\nВведите номер задачи: ')
    task = input('\nОтредактируйте задачу: ')
    status = input('\nСтатус задачи: ')
    with get_connection() as conn:
        storage.edit_task(conn, task, status, id)
    print('\nЗадача отредактирована')



def complite_task():
    task = input ('\nВведите номер задачи: ')
    with get_connection() as conn:
        task = storage.find_all(conn, id)
    print('\nЗадача завершена')


def restart_task():
    task = input ('\nВведите номер задачи: ')
    if not check(conn, id):
        print('Введена неверна задача!')
    with get_connection() as conn:
        task = storage.find_all(conn, id)
    print('\nЗадача возвращена в работу')


def exit():
    sys.exit(0)


def action_show_menu():
    print('''
Ежедневник. Выберите действие:

1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
r. Начать задачу сначала
q. Выход''')


def main():
    with get_connection() as conn: 
        storage.initialize(conn) 

    action_show_menu() 

    actions = {
        '1': list_task,
        '2': add_task,
        '3': edit_task,
        '4': complite_task,
        'r': restart_task,
        'q': exit
    }

    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)
        if actions:
            action()
        else: 
            print('\nНеизвестная команда! ')



