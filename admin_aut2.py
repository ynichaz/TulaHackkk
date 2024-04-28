import sqlite3
from main_bot import user_id

with sqlite3.connect('/Users/varya_kurkubet/Desktop/database.db') as db:
    cursor = db.cursor()
    info = cursor.execute('SELECT * FROM admins WHERE username=?', (user_id,)).fetchone()
    result = ''
    # Если запрос вернул 0 строк, то...
    if info is None:
        result = 'вы не админ'
    else:
        result = 'вы админ! поздравляем!'

db.close()
