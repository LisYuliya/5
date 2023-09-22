# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os


def parse_file_path(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension


file_path = r"C:\Users\User\Downloads\AutoCAD.Civil.3D\Autodesk.AutoCAD.Civil.3D.2018.ru-en.md5"
result = parse_file_path(file_path)

print('Путь до файла: ', result[0])
print('Имя файла: ', result[1])
print('Расширение файла: ', result[2])
