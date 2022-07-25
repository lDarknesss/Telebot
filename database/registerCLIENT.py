import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('registerCLIENT.db')
    cur = base.cursor()
    if base:
        print('База данных регистрации подключена!!!')
    base.execute('CREATE TABLE IF NOT EXISTS clients(name TEXT, surname TEXT PRIMARY KEY, email TEXT, phone TEXT)')
    base.commit()


#добавляем в бд нового клиента
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO clients VALUES(?,?,?,?)', tuple(data.values()))
        base.commit()

#считываем все из бд
async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()