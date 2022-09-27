import os
import pyAesCrypt

def crypter(mode,file):
    password = input("Введите пароль:")#Пароль для шифровки/расшифровки файла
    buffer = 512 * 1024                #Размер буффера(512Кб переведенные в байты
    name = file.split(".")             #Сохраняет имя файла

    if(int(mode)==0):
        pyAesCrypt.encryptFile(file,name[0].lower() + ".html", password,buffer)
    elif(int(mode)==1):
        ftype = input("Введите тип файла: ")
        pyAesCrypt.decryptFile(file,name[0].lower() + "." + ftype,password,buffer)

    os.remove(file)             #Удаляет исходный файл

   
print("0 - Шифровка")
print("1 - Дешифровка")

mode = input("Выберите режим: ")
filename = input("Введите имя файла: ")
crypter(mode,filename)
