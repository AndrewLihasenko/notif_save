""" The script checks the changes in the file by the date and time of saving """

import time
import shelve
import os

filename = r"\\migremont.local\Public\Migremont\Тех. Отдел\Конструкт. бюро\Развертки для лазера\Вопросы по разверткам.xlsx"
# parameter 'r' determine path according to OS
try:
    event_time = os.path.getmtime(filename)
    new_date = time.ctime(event_time)
    db = shelve.open('base')  # creating database
    if db:
        with shelve.open('base') as date:
            for value in date.values():
                old_date = str(value)
                if old_date[2:26] != new_date:
                    print(new_date, "\nВ файле появились новые записи")
                    cmd = "msg * /server:192.168.0.25 В файле 'Вопросы по разверткам.xlsx' появились новые записи"
                    # msg.exe must be in path C:\Windows\SysWOW64
                    os.system(cmd)
                    db['event_time'] = [new_date]
                else:
                    print("Новых записей нет")
    else:
        db['event_time'] = [new_date]
        print("Создана новая база данных")
    db.close()
except FileNotFoundError:
    cmd = "msg * /server:192.168.0.25 Файл 'Вопросы по разверткам.xlsx' не найден!"
    os.system(cmd)



