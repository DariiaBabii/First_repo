# Реалізуйте клас Contacts, який працюватиме з контактами. На першому етапі ми додамо два методи.

# list_contacts повертає список контактів це змінна contacts з поточного екземпляра класу
# add_contacts додає новий контакт до списку, який є змінною об'єкту - contacts
# Клас Contacts містить змінну класу current_id. 
# Ми будемо використовувати її при додаванні нового контакту як унікального ідентифікатора контакту. 
# Коли ми додаємо новий контакт, то передаємо такі аргументи в метод add_contacts: 
# name, phone, email та favorite. 
# Метод повинен створити словник із зазначеними ключами та значеннями параметрів функції. 
# Також необхідно додати до словника новий ключ id, значенням якого є значення змінної класу current_id.
# додамо до класу метод get_contact_by_id. 
# Метод повинен шукати контакт по унікальному id у списку contacts та повертати словник з нього 
# із зазначеним ключем id. Якщо словника із зазначеним id у списку contacts не знайдено, метод повертає None.

# додамо до класу метод remove_contacts. Метод повинен видаляти контакт по унікальному id у списку contacts. 
# Якщо словника із зазначеним id у списку contacts не знайдено, метод жодних дій над списком contacts не робить.
# Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts
        

    def add_contacts(self, name, phone, email, favorite):
        new_contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(new_contact)
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact["id"] == id:
                return contact
        return None
    
    # або отак:
    # def get_contact_by_id(self, id):
    #     result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
    #     return result[0] if len(result) > 0 else None
    
    def remove_contacts(self, id):
        for contact in self.contacts:
            if contact["id"] == id:
                self.contacts.remove(contact)
                return True
        return False
    def remove_contacts(self, id):
    contact = self.get_contact_by_id(id)
    if contact:
        self.contacts.remove(contact)
        return contact
    return None

        
            
                
                
                
                
                
            
        
        
