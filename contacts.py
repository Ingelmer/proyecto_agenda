''''
Aplicación para guardar contactos y mostrarlos en consola

'''

import csv
from Clases.contactbook import ContactBook
def run():
    contac_book = ContactBook()
    with open('contacts.csv','r') as f:
        reader = csv.reader(f)
        for idx,row in enumerate(reader):
            if idx == 0:
                continue
            contac_book.add(row[0],row[1],row[2])

    while True:
        command = str(input('''
        ¿Qué deseas hacer ?
        
        [a]ñadir contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]alir
        '''))
        if command == 'a':
            name = str(input('Escribe el nombre de contacto'))
            phone = str(input('Escribe el tel de contacto'))
            mail = str(input('Escribe el email de contacto'))
            contac_book.add(name,phone,mail)
        elif command == 'ac':
            name = str(input('Escribe el nombre de contacto'))
            contac_book.update(name)
        elif command == 'b':
            name = str(input('Escribe el nombre de contacto'))
            contac_book.search(name) 
        elif command == 'e':
            name = str(input('Escribe el nombre de contacto'))
            contac_book.delete(name)    
        elif command == 'l':
            contac_book.show_all()
        elif command == 's':
            break

if __name__ == '__main__':
    print('BIENVENIDO A SU AGENDA')
    run()