import sqlite3
import os.path as Path
conn = sqlite3.connect('base.db')
cur = conn.cursor()


SQL_SELECT_ALL = '''
    SELECT
        id, task, status
    FROM
        base
'''

SQL_SELECT_TASK_BY_ID = SQL_SELECT_ALL + ' WHERE id = %s'

SQL_INSERT_ADD_TASK = '''
    INSERT INTO base (task, status)
    VALUES (?, ?)
'''

SQL_EDIT_TASK = '''
    UPDATE base 
    SET task = '?', status = '?'
    WHERE ID = ?
'''

SQL_COMPLITE_TASK = '''
    UPDATE base 
    SET status = 'Задача выполнена'
    WHERE ID = ?
    '''

SQL_RESTART_TASK = '''
    UPDATE base 
    SET status = 'Задача вернулась в работу'
    WHERE ID = ?
'''

def dict_factory(cursor, row):
    d = {}
    print('row:', row)
    print('col:', cursor.description)
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx] 
    return d


def connect (db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn


def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'shema.sql')
        with open (script_file_path) as f:
            conn.executescript(f.read())

def find_all(conn):
    with conn:
        cur = conn.execute(SQL_SELECT_ALL)
        return cur.fetchall()


def list_task(conn):
    with conn:
        cur = conn.execute(SQL_SELECT_ALL)
        return c.fetchall()


def add_task(conn, task, status):
    with conn:
        cur = conn.execute(SQL_INSERT_ADD_TASK, (task, status))


def edit_task(conn, id, task, status):
    with conn:
        cur = conn.execute(SQL_EDIT_TASK, (task, status, id))


def complite_task(conn, id):
    with conn:
        cur = conn.execute(SQL_COMPLITE_TASK, id)

        
def restart_task(conn, id):
    with conn:
        cur = conn.execute(SQL_RESTART_TASK, id)        


def exit():
    sys.exit(0)                 


def check(conn, id):
    with conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_ID, id)