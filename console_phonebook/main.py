import json


def welcome_eng():
    print(" Welcome to the Phonebook App ".center(68, "*"))
    print(' Menu '.center(68, '*'))
    while True:
        try:
            choice = int(input("1) Create a contact \n2) Search a contact \n3) List all contacts \n"
                               "4) Change language - Dil değiştir(Türkçe) - Sprache ändern(Deutsch)\n5) Exit\n"
                               "Please choose an option from the menu and type the number: "))
        except:
            print("Type a number please")
            continue
        if choice < 1 or choice > 5:
            print("Your choice must be a number between (1-5)")
        elif choice == 5:
            exit()
        elif choice == 1:
            create_contact()
        elif choice == 2:
            search_contact()
        elif choice == 3:
            list_contacts()
        elif choice == 4:
            change_lang()


def welcome_tr():
    print(" Telefon Defterine hoş geldiniz ".center(68, "*"))
    print(' Menü '.center(68, '*'))
    while True:
        try:
            choice = int(input("1) Kişi ekle \n2) Kişi ara \n3) Kişileri listele \n"
                               "4) Change language - Dil değiştir(Türkçe) - Sprache ändern(Deutsch)\n5) Çıkış\n"
                               "Lütfen seçiminizin numarasını tuşlayın: "))
        except:
            print("Lütfen bir sayı girin")
            continue
        if choice < 1 or choice > 5:
            print("Girdiğiniz sayı yanlış! (1-5) aralğında olmalı")
        elif choice == 5:
            exit()
        elif choice == 1:
            create_contact_tr()
        elif choice == 2:
            search_contact_tr()
        elif choice == 3:
            list_contacts_tr()
        elif choice == 4:
            change_lang()


def welcome_de():
    # adding a german language choice to the menu

    pass


def create_contact():
    print(" Please type the information about the new contact ".center(68, "*"))
    name = input("Name: ")
    surname = input("Surname: ")
    phone = input("Phone Number: ")
    workplace = input("Workplace: ")
    note = input("Type your notes about the contact: ")
    contact_info = ('{' + '"name"' + ': ' + f'"{name}"' + ', ' + '"surname"' + ': ' + f'"{surname}"' + ', '
                    + '"phone"' + ': ' + f'"{phone}"' + ', ' + '"workplace"' + ': ' + f'"{workplace}"' + ', '
                    + '"note"' + ': ' + f'"{note}"' + '}' + '\n')

    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        lines.append(contact_info)
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
    print(f"'{name} {surname}' added to the phonebook")
    print(68 * "*")
    while True:
        try:
            choice = int(input("1) Add new contact\n2) Return to the Menu\n "
                               "Please choose an option and type the number: "))
        except:
            print("Type a number please")
            return
        if choice < 1 or choice > 2:
            print("Your choice must be a number between (1-2)")
        elif choice == 1:
            create_contact()
        elif choice == 2:
            welcome_eng()


def create_contact_tr():
    print(" Lütfen yeni kişi hakkındaki bilgileri girin ".center(68, "*"))
    name = input("İsim: ")
    surname = input("Soyisim: ")
    phone = input("Telefon Numarası: ")
    workplace = input("İşveren: ")
    note = input("Kişi hakkında bilgiler: ")
    contact_info = ('{' + '"name"' + ': ' + f'"{name}"' + ', ' + '"surname"' + ': ' + f'"{surname}"' + ', '
                    + '"phone"' + ': ' + f'"{phone}"' + ', ' + '"workplace"' + ': ' + f'"{workplace}"' + ', '
                    + '"note"' + ': ' + f'"{note}"' + '}' + '\n')

    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        lines.append(contact_info)
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
    print(f"'{name} {surname}' Telefon defterine eklendi")
    print(68 * "*")
    while True:
        try:
            choice = int(input("1) Yeni kişi ekle\n2) Ana Menüye dön\n "
                               "Lütfen birini seçip, sayıyı giriniz: "))
        except:
            print("Lütfen sayı girin")
            return
        if choice < 1 or choice > 2:
            print("Girdiğiniz sayı yanlış! (1-2) aralğında olmalı")
        elif choice == 1:
            create_contact_tr()
        elif choice == 2:
            welcome_tr()


def search_contact():
    while True:
        search_text = input("Type letters what you want to find in phonebook: ").lower()
        with open("contacts.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            screen_list = []
            count = 1
            for line in lines:
                result = json.loads(line)
                if search_text in (result["name"]).lower():
                    if line not in screen_list:
                        screen_list.append(line)
            for line in lines:
                result = json.loads(line)
                if search_text in (result["surname"]).lower():
                    if line not in screen_list:
                        screen_list.append(line)
            for line in lines:
                result = json.loads(line)
                if search_text in result["phone"]:
                    if line not in screen_list:
                        screen_list.append(line)
            for line in lines:
                result = json.loads(line)
                if search_text in (result["workplace"]).lower():
                    if line not in screen_list:
                        screen_list.append(line)
            for line in lines:
                result = json.loads(line)
                if search_text in (result["note"]).lower():
                    if line not in screen_list:
                        screen_list.append(line)
            if len(screen_list) == 0:
                print(f"'{search_text}' can not found in Phonebook")
                break
            else:
                for line in screen_list:
                    result = json.loads(line)
                    print(f'{count}- {result["name"]} {result["surname"]} {result["phone"]}')
                    count += 1
        while True:
            select = input("Press 'M' to return Menu\nFor details, type the number of the contact from list:  ")
            if select == "m" or select == "M":
                welcome_eng()
            try:
                select = int(select)
            except:
                print("Type the number of the contact please")
                continue
            if select < 1 or select > len(screen_list):
                print(f"Your select must be a number between (1-{len(screen_list)})")
                continue
            elif 1 <= select <= len(screen_list):
                with open("contacts.txt", "r", encoding="utf-8") as file:
                    lines = file.readlines()
                    last_count = 1
                    for line in lines:
                        if screen_list[select - 1] in line:
                            choice = last_count
                            contact_detail(choice)
                        else:
                            last_count += 1


def search_contact_tr():
    while True:
        search_text = input("Telefon Defterinde aradığız harfleri girin: ").lower()
        with open("contacts.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            screen_list = []
            count = 1
            for line in lines:
                result = json.loads(line)
                if search_text in (result["name"]).lower():
                    if line not in screen_list:
                        screen_list.append(line)
            for line in lines:
                result = json.loads(line)
                if search_text in (result["surname"]).lower():
                    if line not in screen_list:
                        screen_list.append(line)
            for line in lines:
                result = json.loads(line)
                if search_text in result["phone"]:
                    if line not in screen_list:
                        screen_list.append(line)
            for line in lines:
                result = json.loads(line)
                if search_text in (result["workplace"]).lower():
                    if line not in screen_list:
                        screen_list.append(line)
            for line in lines:
                result = json.loads(line)
                if search_text in (result["note"]).lower():
                    if line not in screen_list:
                        screen_list.append(line)
            if len(screen_list) == 0:
                print(f"'{search_text}' rehberde bulunamadı")
                break
            else:
                for line in screen_list:
                    result = json.loads(line)
                    print(f'{count}- {result["name"]} {result["surname"]} {result["phone"]}')
                    count += 1
        while True:
            select = input("Menüye dönmek için 'M' tuşlayın \n"
                           "Ayrıntılar için, seçtiğiniz kişinin listedeki numarasını girin:  ")
            if select == "m" or select == "M":
                welcome_tr()
            try:
                select = int(select)
            except:
                print("Kişinin listedeki sayısını girin")
                continue
            if select < 1 or select > len(screen_list):
                print(f"Seçiminiz (1-{len(screen_list)}) aralığında olmalı")
                continue
            elif 1 <= select <= len(screen_list):
                with open("contacts.txt", "r", encoding="utf-8") as file:
                    lines = file.readlines()
                    last_count = 1
                    for line in lines:
                        if screen_list[select - 1] in line:
                            choice = last_count
                            contact_detail_tr(choice)
                        else:
                            last_count += 1


def list_contacts():
    print(" List of contacts ".center(68, "*"))
    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        count = 1
        for line in lines:
            result = json.loads(line)
            print(f'{count}- {result["name"]} {result["surname"]} {result["phone"]}')
            count += 1
    while True:
        choice = input("Press 'M' to return Menu\nFor details, type the number of the contact from list:  ")
        if choice == "m" or choice == "M":
            welcome_eng()
        try:
            choice = int(choice)
        except:
            print("Type the number of the contact please")
            continue
        if choice < 1 or choice > len(lines):
            print(f"Your choice must be a number between (1-{len(lines)})")
            continue
        elif 1 <= choice <= len(lines):
            return contact_detail(choice)


def list_contacts_tr():
    print(" Kişi Listesi ".center(68, "*"))
    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        count = 1
        for line in lines:
            result = json.loads(line)
            print(f'{count}- {result["name"]} {result["surname"]} {result["phone"]}')
            count += 1
    while True:
        choice = input("Menüye dönmek için 'M' tuşlayın \n"
                       "Ayrıntılar için, seçtiğiniz kişinin listedeki numarasını girin:    ")
        if choice == "m" or choice == "M":
            welcome_tr()
        try:
            choice = int(choice)
        except:
            print("Kişinin listedeki sayısını girin")
            continue
        if choice < 1 or choice > len(lines):
            print(f"Seçiminiz (1-{len(lines)}) aralığında olmalı")
            continue
        elif 1 <= choice <= len(lines):
            return contact_detail_tr(choice)


def contact_detail(choice):
    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        line_list = []
        for line in lines:
            result = json.loads(line)
            line_list.append(result)
        print(" Details About ".center(40, "*"))
        print(f' {line_list[choice - 1]["name"]} {line_list[choice - 1]["surname"]} '.center(40, " "))
        print(f'Phone Number: {line_list[choice - 1]["phone"]}')
        print(f'Workplace   : {line_list[choice - 1]["workplace"]}')
        print(f'About       : {line_list[choice - 1]["note"]}')
        print('_'.center(40, "_"))
        while True:
            try:
                select = int(
                    input(f'1) Edit contact "{line_list[choice - 1]["name"]} {line_list[choice - 1]["surname"]}"'
                          f'\n2) Delete contact "{line_list[choice - 1]["name"]} '
                          f'{line_list[choice - 1]["surname"]}"\n3) Return to the Menu\n'
                          'Please choose an option and type the number: '))
            except:
                print("Type a number please")
                continue
            if select < 1 or select > 3:
                print("Your choice must be a number between (1-3)")
            elif select == 1:
                edit_contact(choice)
            elif select == 2:
                del_contact(choice)
            elif select == 3:
                welcome_eng()


def contact_detail_tr(choice):
    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        line_list = []
        for line in lines:
            result = json.loads(line)
            line_list.append(result)
        print(" Ayrıntılar ".center(40, "*"))
        print(f' {line_list[choice - 1]["name"]} {line_list[choice - 1]["surname"]} '.center(40, " "))
        print(f'Telefon Numarası  : {line_list[choice - 1]["phone"]}')
        print(f'İşveren           : {line_list[choice - 1]["workplace"]}')
        print(f'Hakkında          : {line_list[choice - 1]["note"]}')
        print('_'.center(40, "_"))
        while True:
            try:
                select = int(
                    input(f'1) Kişiyi Güncelle"{line_list[choice - 1]["name"]} {line_list[choice - 1]["surname"]}"'
                          f'\n2) Kişiyi sil "{line_list[choice - 1]["name"]} '
                          f'{line_list[choice - 1]["surname"]}"\n3) Ana Menüye dön\n'
                          'Lütfen seçin ve sayısını yazıp "Enter" tuşuna basın: '))
            except:
                print("Lütfen sayı girin")
                continue
            if select < 1 or select > 3:
                print("Seçiminiz (1-3) aralığında olmalı")
            elif select == 1:
                edit_contact_tr(choice)
            elif select == 2:
                del_contact_tr(choice)
            elif select == 3:
                welcome_tr()


def edit_contact(choice):
    print(" Please type the new information about the contact ".center(68, "*"))
    name = input("Name: ")
    surname = input("Surname: ")
    phone = input("Phone Number: ")
    workplace = input("Workplace: ")
    note = input("Type your notes about the contact: ")
    contact_info = ('{' + '"name"' + ': ' + f'"{name}"' + ', ' + '"surname"' + ': ' + f'"{surname}"' + ', '
                    + '"phone"' + ': ' + f'"{phone}"' + ', ' + '"workplace"' + ': ' + f'"{workplace}"' + ', '
                    + '"note"' + ': ' + f'"{note}"' + '}' + '\n')

    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        del lines[choice - 1]
        lines.insert((choice - 1), contact_info)
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
    print("Contact updated")
    print(68 * "*")
    list_contacts()


def edit_contact_tr(choice):
    print(" Lütfen kişi hakkındaki yeni bilgileri giriniz ".center(68, "*"))
    name = input("İsim: ")
    surname = input("Soyisim: ")
    phone = input("Telefon Numarası: ")
    workplace = input("İşveren: ")
    note = input("Kişi hakkındaki bilgiler: ")
    contact_info = ('{' + '"name"' + ': ' + f'"{name}"' + ', ' + '"surname"' + ': ' + f'"{surname}"' + ', '
                    + '"phone"' + ': ' + f'"{phone}"' + ', ' + '"workplace"' + ': ' + f'"{workplace}"' + ', '
                    + '"note"' + ': ' + f'"{note}"' + '}' + '\n')

    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        del lines[choice - 1]
        lines.insert((choice - 1), contact_info)
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
    print("Kişi güncellendi")
    print(68 * "*")
    list_contacts_tr()


def del_contact(choice):
    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        del lines[choice - 1]
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
    print("Contact deleted")
    print(68 * "*")
    list_contacts()


def del_contact_tr(choice):
    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        del lines[choice - 1]
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
    print("Kişi silindi")
    print(68 * "*")
    list_contacts_tr()


def change_lang():
    print("*".center(68, "*"))
    while True:
        try:
            choice = int(input("1) English \n2) Türkçe - Turkish \n3) Return to the Menu \n"
                               "4) Exit\n"
                               "Lütfen Türkçe için '2' yazıp 'Enter' tuşuna basın: \n"
                               "Please choose an option from the menu and type the number: "))
        except:
            print("Type a number please-Lütfen sayı girin")
            continue
        if choice < 1 or choice > 4:
            print("Your choice must be a number between (1-3)-Seçiminiz (1-3) aralığında olmalı")
        elif choice == 4:
            exit()
        elif choice == 1:
            welcome_eng()
        elif choice == 2:
            welcome_tr()
        elif choice == 3:
            welcome_eng()


while True:
    welcome_eng()
