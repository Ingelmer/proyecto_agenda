import csv
class Contact:

    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email  = email

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self,name,phone,email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()
        
    def show_all(self):
        if self._contacts:
            for contact in self._contacts:
                self._print_contact(contact)
        else:
            self._not_found('Agenda vacía')

    def _print_contact(self,contact):
        print('--- * --- * --- * --- * --- * --- * --- * --- *')
        print('Nombre: {}'.format(contact.name))
        print('Phone: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * --- *')

    def delete(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
    def search(self,name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found('Archivo no encontrado')

    def update(self,name):

        while True:
            idx = self._privated_search(name)
            if idx != -1:
                self._print_contact(self._contacts[idx])
                feature = str(input('''Que característica desea actualizar?
                [n]ombre
                [t]elefono
                [e]mail
                
                [s]alir
                '''))

                if feature.lower() == 'n':
                    nombre = str(input('Escriba el nuevo nombre: '))
                    self._contacts[idx].name = nombre
                    self._save()
                    name = nombre
                elif feature == 't':
                    phone = str(input('Ingrese el nuevo telefono: '))
                    self._contacts[idx].phone = phone
                    self._save()
                elif feature == 'e':
                    email = str(input('Ingrese el nuevo email: '))
                    self._contacts[idx].email = email
                    self._save()
                elif feature == 's':
                    break
                else:
                    self._not_found('Opcion no encontrada, seleccione otra')
            else:
                self._not_found('Contacto no encontrado')
                break

    def _privated_search(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                return idx
        else:
            return -1
    def _save(self):        
        with open('contacts.csv','w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))
    def _not_found(self,message):
        print('********************************')
        print(message)
        print('********************************')