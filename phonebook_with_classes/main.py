from phonebook import Contact
from phonebook import Phonebook


def load_bot_instances():
    c1 = Contact(name="Kel", surname="Mahmut", phone="Test", workplace="Test", note="Test")
    c2 = Contact(name="Hafize", surname="Ana", phone="Test2", workplace="Test2", note="Test2")
    c3 = Contact(name="Badi", surname="Ekrem", phone="Test3", workplace="Test3", note="Test3")
    c4 = Contact(name="İnek", surname="Şaban", phone="Test4", workplace="Test4", note="Test4")
    c5 = Contact(name="Damat", surname="Ferit", phone="Test5", workplace="Test5", note="Test5")
    c6 = Contact(name="Güdük", surname="Necmi", phone="Test6", workplace="Test6", note="Test6")
    c7 = Contact(name="Hayta", surname="İsmail", phone="Test7", workplace="Test7", note="Test7")
    c8 = Contact(name="Tulum", surname="Hayri", phone="Test8", workplace="Test8", note="Test8")
    c9 = Contact(name="Domdom", surname="Ali", phone="Test9", workplace="Test9", note="Test9")
    c10 = Contact(name="Paşa", surname="Nuri", phone="Test10", workplace="Test10", note="Test10")
    Contact.contacts_list.append(c1)
    Contact.contacts_list.append(c2)
    Contact.contacts_list.append(c3)
    Contact.contacts_list.append(c4)
    Contact.contacts_list.append(c5)
    Contact.contacts_list.append(c6)
    Contact.contacts_list.append(c7)
    Contact.contacts_list.append(c8)
    Contact.contacts_list.append(c9)
    Contact.contacts_list.append(c10)
    print("10 Contacts added")


def welcome():
    print("\n ")
    print(" Welcome to the phonebook App ".center(88, " "))
    while True:
        selection = input("""
                              ----MENU----
                          1: Create a contact
                          2: Search a contact
                          3: List all contacts
                          4: Change language-Dil değiştir(Türkçe)
                          5: Load bot Contacts
                          6: Exit
                          

                          Please choose an option from the menu and type the number: """)
        print(' ')

        if selection == '1':
            Contact.create_contact()
        elif selection == '2':
            Phonebook.search_contact()
        elif selection == '3':
            Phonebook.list_contacts()
        elif selection == '4':
            pass
        elif selection == '5':
            load_bot_instances()
        elif selection == '6':
            quit()
        else:
            print('Please choose a valid number')


welcome()
