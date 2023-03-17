# Задача 38
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

import os

tel_base = r'C:\Users\Петровна\Desktop\GB_home\Python\H.W.#8\tel_base.txt'

def append_contact(tel_base):
    contact = input('Введите контакт в формате ФИО номер телефона:')
    with open(tel_base, 'a', encoding='utf-8') as f:
        f.write(f'\n{contact}')
    print('Контакт добавлен')

def read_file(tel_base):
    with open(tel_base, 'r', encoding='utf-8') as f:
        print(f.read())

def search_contact(tel_base):
    search = input('Введите информацию для поиска(фамилию, имя, отчество, номер телефона):')
    with open(tel_base, 'r', encoding='utf-8') as f:
        for line in f:
            if search in line:
                print(line)

def change_contact(tel_base):
    search = input('Введите информацию для поиска(фамилию, имя, отчество, номер телефона):')
    with open(tel_base, 'r', encoding='utf-8') as f:
        for line in f:
            if search in line:
                old_contact = line
                new_contact = input('Введите информацию для изменения:')
                with open (tel_base, 'r', encoding='utf-8') as f:
                    old_base = f.read()
                    new_base = old_base.replace(old_contact, f'{new_contact}\n')
                with open (tel_base, 'w', encoding='utf-8') as f:
                    f.write(new_base)
                print('Контакт изменен')

def delete_contact(tel_base):
    search = input('Введите информацию для поиска(фамилию, имя, отчество, номер телефона):')
    with open(tel_base, 'r', encoding='utf-8') as f:
        for line in f:
            if search in line:
                with open (tel_base, 'r', encoding='utf-8') as f:
                    new_base = f.readlines()
                with open (tel_base, 'w', encoding='utf-8') as f:
                    for line in new_base:
                        if search not in line:
                            f.write(line)
                    print('Контакт удален')

def user_interface():
    print('Добро пожаловать! \n1)Вывести весь справочник \n2)Добавить контакт \n3)Найти контакт \n4)Изменить контакт \n5)Удалить контакт')
    while (input1 := int(input('Выберите действие (Для выхода нажмите 0): '))) != 0:
        if input1 == 1: 
            read_file(tel_base)
        elif input1 == 2: 
            append_contact(tel_base)
        elif input1 == 3:
            search_contact(tel_base)
        elif input1 == 4:
            change_contact(tel_base)
        elif input1 == 5:
            delete_contact(tel_base)
        else:
            print('Некоректный ввод')

user_interface()