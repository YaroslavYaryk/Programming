import pyAesCrypt
import os
import sys

# функция дешифровки файла
def decryption(file, password):

    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")

    # удаляем исходный файл
    os.remove(file)

password = input("Введите пароль для шифрования: ")
path = "D:\Desktop\Education\English\Dyhanov.txt.crp"
decryption(path, password)