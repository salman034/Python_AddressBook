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


if __name__ == "__main__":
    print("Welcome to address book")
    contact_list = []
    while True:
        user_input = int(
            input("Enter your choice\n1:Add the contact\n2:Edit the contact\n3:Delete the contact\n4:Display"
                  "\n5:Exit: "))
        if user_input == 1:
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            address = input("Enter the address: ")
            city = input("Enter the city: ")
            state = input("Enter the state: ")
            pincode = input("Enter the pin code: ")
            email = input("Enter email id: ")
            mobile_number = input("Enter mobile number: ")
            result = Contact(f_name, l_name, address, city, state, pincode, email, mobile_number)
            contact_list.append(result.details)
            print(contact_list)
        elif user_input == 2:
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
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
            print(contact_list)
        elif user_input == 5:
            sys.exit()