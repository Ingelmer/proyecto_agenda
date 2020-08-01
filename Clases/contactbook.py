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
        #print('name: {}, phone: {}, email {}'.format(name,phone,email))
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
    def _print_contact(self,contact):
        print('--- * --- * --- *---*---*---*---*---*')
        print('Nombre: {}'.format(contact.name))
        print('Phone: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- *---*---*---*---*---*')

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
        idx = self._privated_search(name)
        if idx != -1:
            self._print_contact(self._contacts[idx])
            feature = str(input('Escriba la caracteristica a actualizar: '))
            if feature.lower() == 'Nombre'.lower():
                nombre = str(input('Escriba el nuevo nombre: '))
                self._contacts[idx].name = nombre
                self._save()
                #contact.name = nombre
            elif feature == 'Phone'.lower():
                phone = str(input('Ingrese el nuevo telefono'))
                self._contacts[idx].phone = phone
                self._save()
            elif feature == 'Email'.lower():
                email = str(input('Ingrese el nuevo email'))
                self._contacts[idx].email = email
                self._save()
            else:
                self._not_found('Caracteristica no encontrada')
        else:
            self._not_found('Contacto no encontrado')
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