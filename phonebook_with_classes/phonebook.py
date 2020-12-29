
class Contact:
    contacts_list = []

    def __init__(self, name="null", surname="null", phone="null", workplace="No Information", note="No Data"):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.workplace = workplace
        self.note = note

    def contact_details(instance):
        print(" Details About ".center(40, "*"))
        print(f' {instance.name} {instance.surname} '.center(40, " "))
        print(f'Phone Number: {instance.phone}')
        print(f'Workplace   : {instance.workplace}')
        print(f'About       : {instance.note}')
        print('_'.center(40, "_"))
        while True:
            try:
                select = int(
                    input(
                        f'1) Edit contact "{instance.name} {instance.surname}"'
                        f'\n2) Delete contact "{instance.name} '
                        f'{instance.surname} "\n3) Return to the Menu\n'
                        'Please choose an option and type the number: '))
            except:
                print("Type a number please: ")
                continue
            if select < 1 or select > 3:
                print("Your choice must be a number between (1-3)")
            elif select == 1:
                Contact.edit_contact(instance)
            elif select == 2:
                Contact.del_contact(instance)
            elif select == 3:
                import main
                main.welcome()

    def give_me_instance(text):
        for i in Contact.contacts_list:
            if text == f'{i.name} {i.surname} - Phone : {i.phone}':
                return Contact.contact_details(instance=i)

    @staticmethod
    def create_contact(name="null", surname="null", phone="null", workplace="No Information", note="No Data"):
        print(" Please type the information about the new contact ".center(68, "*"))
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone Number: ")
        workplace = input("Workplace: ")
        note = input("Type your notes about the contact: ")

        naming = 'instance_' + str(len(Contact.contacts_list))
        globals()[naming] = Contact(name, surname, phone, workplace, note)
        Contact.contacts_list.append(globals()[naming])
        print(f"Contact created: {name} {surname}")

    def edit_contact(intance):
        print(" Please type the new information about the contact ".center(68, "*"))
        intance.name = input("Name: ")
        intance.surname = input("Surname: ")
        intance.phone = input("Phone Number: ")
        intance.workplace = input("Workplace: ")
        intance.note = input("Type your notes about the contact: ")
        print("Contact updated")
        print(68 * "*")
        import main
        main.welcome()

    def del_contact(intance):
        intance.name = ""
        intance.surname = ""
        intance.phone = ""
        intance.workplace = ""
        intance.note = ""

        print("Contact deleted")
        print(68 * "*")
        import main
        main.welcome()


class Phonebook:

    def __init__(self, name="null", surname="null", phone="null"):
        self.name = name
        self.surname = surname
        self.phone = phone

    @staticmethod
    def list_contacts():
        if len(Contact.contacts_list) == 0:
            print("Unfortunately Phonebook is empty! You can create contacts or load bots from menu:)")
            import main
            main.welcome()
        print(" List of contacts ".center(48, "*"))
        count = 1
        unsorted_list = []
        for instance in Contact.contacts_list:
            if instance.name == "" and instance.surname == "" and instance.phone == "":
                continue
            else:
                unsorted_list.append(f'{instance.name} {instance.surname} - Phone : {instance.phone}')
        for i in sorted(unsorted_list):
            print(f'{count}- {i}')
            count += 1

        while True:
            choice = input("Press 'M' to return Menu\nFor details, type the number of the contact from list:  ")
            if choice == "m" or choice == "M":
                import main
                main.welcome()
            try:
                choice = int(choice)
            except:
                print("Type the number of the contact please")
                continue
            if choice < 1 or choice > len(unsorted_list):
                print(f"Your choice must be a number between (1-{len(unsorted_list)})")
                continue
            elif 1 <= choice <= len(unsorted_list):
                return Contact.give_me_instance(text=(sorted(unsorted_list))[choice - 1])

    @staticmethod
    def search_contact():
        while True:
            print('If you want to return to the menu type: "M" ')
            search_text = input("Type letters what you want to find in phonebook: ").lower()
            if search_text == "m":
                import main
                main.welcome()
            screen_list = []
            count = 1
            for instance in Contact.contacts_list:
                if search_text in (instance.name).lower():
                    if instance not in screen_list:
                        screen_list.append(instance)
            for instance in Contact.contacts_list:
                if search_text in (instance.surname).lower():
                    if instance not in screen_list:
                        screen_list.append(instance)
            for instance in Contact.contacts_list:
                if search_text in instance.phone:
                    if instance not in screen_list:
                        screen_list.append(instance)
            for instance in Contact.contacts_list:
                if search_text in (instance.workplace).lower():
                    if instance not in screen_list:
                        screen_list.append(instance)
            for instance in Contact.contacts_list:
                if search_text in (instance.note).lower():
                    if instance not in screen_list:
                        screen_list.append(instance)
            if len(screen_list) == 0:
                print(f"'{search_text}' can not found in phonebook")
                continue
            else:
                for instance in screen_list:
                    print(f'{count}- {instance.name} {instance.surname} {instance.phone}')
                    count += 1
                break
        while True:
            selection = input("Press 'M' to return Menu\nFor details, type the number of the contact from list:  ")
            if selection == "m" or selection == "M":
                import main
                main.welcome()
            try:
                selection = int(selection)
            except:
                print("Type the number of the contact please")
                continue
            if selection < 1 or selection > len(screen_list):
                print(f"Your select must be a number between (1-{len(screen_list)})")
                continue
            elif 1 <= selection <= len(screen_list):
                print(screen_list[selection - 1].name)
                Contact.contact_details(instance=screen_list[selection - 1])

