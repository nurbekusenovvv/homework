# sql=СУДБ
# система управления базами данных
# db
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn=sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn,sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

def create_student(conn,student):
    sql = '''INSERT INTO student(name,mark,hobby,date,is_working)
    VALUES(?,?,?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,student)
        conn.commit()
    except Error as e:
        print(e)


database=f'group04-1.db'

sql_create_students_table='''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR (20) NOT NULL ,
mark INTEGER NOT NULL DEFAULT 0,
hobby TEXT DEFAULT NULL,
date DATE NOT NULL,
is_working BOOLEAN DEFAULT FALSE
);
'''


connection=create_connection(database)
if connection is not None:
    print('всё работает')

    # create_table(connection,sql_create_students_table)
    create_student(connection,('alien',7,None,'01-01-01',True))