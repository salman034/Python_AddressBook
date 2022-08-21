import sys


class Contact:
    def __init__(self, first_name, last_name, address, city, state, pin_code, email_id, mobile_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.pin_code = pin_code
        self.email_id = email_id
        self.mobile_number = mobile_number
        self.details = [self.first_name, self.last_name, self.address, self.city, self.state, self.pin_code,
                        self.email_id, self.mobile_number]


def add(name):
    local = []
    temp = addressbook.get(name)
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    address = input("Enter the address: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    pincode = input("Enter the pin code: ")
    email = input("Enter email id: ")
    mobile_number = input("Enter mobile number: ")
    temp1 = []
    if temp:
        for i in addressbook.get(name):
            temp1.append(i)
        for i in temp:
            if email == i[6] or mobile_number == i[7]:
                print("user name already exist")
            else:
                result = Contact(f_name, l_name, address, city, state, pincode, email, mobile_number)
                temp1.append(result.details)
                temp1.sort()
                addressbook[name] = temp1
                print("Contact Added Successfully")
    else:
        result = Contact(f_name, l_name, address, city, state, pincode, email, mobile_number)
        local.append(result.details)
        addressbook[name] = local
        print("Contact added successfully")


def edit(name):
    f_name = input("Enter First Name: ")
    l_name = input("Enter Last Name: ")
    contact_list = addressbook.get(name)
    for i in contact_list:
        if f_name == i[0] and l_name == i[1]:
            print("Contact found, please enter details to update")
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            address = input("Enter the address: ")
            city = input("Enter the city: ")
            state = input("Enter the state: ")
            pincode = input("Enter the pin code: ")
            email = input("Enter email id: ")
            mobile_number = input("Enter mobile number: ")
            index = contact_list.index(i)
            contact_list[index] = [f_name, l_name, address, city, state, pincode, email, mobile_number]
            addressbook[name] = contact_list


def book_entry(name):
    print(name)
    while True:
        user_input = int(
            input("Enter your choice to continue..\n1:Add the Contact\n2:Edit the Contact\n3:Delete the Contact\n4:Display"
                  "\n5:Return to Main Menu: "))
        if user_input == 1:
            add(name)
        elif user_input == 2:
            edit(name)
            print("Contact edited successfully")
        elif user_input == 3:
            f_name = input("Enter First Name: ")
            l_name = input("Enter Last Name: ")
            temp = addressbook.get(name)
            for i in temp:
                if f_name == i[0] and l_name == i[1]:
                    temp.remove(i)
            print("Contact deleted successfully")
        elif user_input == 4:
            print(addressbook.get(name))
        elif user_input == 5:
            main_menu()


def search_by_city(list, name):
    temp = []
    for i in list:
        if i[3] == name:
            temp.append(i)
    print(temp)
    print(f"number of person in {name} is: ", len(temp))


def search_by_state(list, name):
    temp = []
    for i in list:
        if i[4] == name:
            temp.append(i)
    print(temp)
    print(f"number of person in {name} is: ", len(temp))


def sort_by_city(list):
    list.sort()
    print(list)


def main_menu():
    while True:
        menu = int(input("Enter Your Choice to Continue..\n1 : Create NewBook\n2 : Access the existing Address Book\n"
                         "3 : Display all Books\n4 : Search Person by City\n5 : Search Person by State\n6 : Sort by City"
                         "\n7 : Sort by State\n8 : Sort by Pincode\n9 : Exit: "))
        if menu == 1:
            book_name = input("Enter Name of the Book: ")
            if addressbook:
                for i in addressbook:
                    if i == book_name:
                        print("Name already exist please enter another name")
                        main_menu()
                    else:
                        book_entry(book_name)
            else:
                book_entry(book_name)
        elif menu == 2:
            name = input("Enter name of the book you are searching for: ")
            book_entry(name)
        elif menu == 3:
            print(addressbook)
        elif menu == 4:
            city_name = input("Enter Name of the city: ")
            temp = []
            for j in addressbook.keys():
                for i in addressbook.get(j):
                    temp.append(i)
            search_by_city(temp, city_name)
        elif menu == 5:
            state_name = input("Enter name of the city: ")
            temp = []
            for j in addressbook.keys():
                for i in addressbook.get(j):
                    temp.append(i)
            search_by_state(temp, state_name)
        elif menu == 6:
            temp = []
            for j in addressbook.keys():
                for i in addressbook.get(j):
                    temp.append(i)
            temp.sort(key=lambda x: x[3])
            print(temp)
        elif menu == 7:
            temp = []
            for j in addressbook.keys():
                for i in addressbook.get(j):
                    temp.append(i)
            temp.sort(key=lambda x: x[4])
            print(temp)
        elif menu == 8:
            temp = []
            for j in addressbook.keys():
                for i in addressbook.get(j):
                    temp.append(i)
            temp.sort(key=lambda x: x[5])
            print(temp)
        elif menu == 9:
            sys.exit()


if __name__ == "__main__":
    print("|...Welcome to Address Book...|")
    addressbook = {}
    main_menu()