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

        details = [self.first_name, self.last_name, self.address, self.city, self.state, self.pin_code,
                   self.email_id, self.mobile_number]

        print(details)


if __name__ == "__main__":
    print("Welcome to address book")
    user_input = int(input("Enter your choice\n1:Add the contact\n2:Edit the contact\n3:Delete the contact\n4:display"
                           "\n5:exit: "))
    if user_input == 1:
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        address = input("Enter the address: ")
        city = input("Enter the city: ")
        state = input("Enter the state: ")
        pincode = input("Enter the pin code: ")
        email = input("Enter email id: ")
        mobile_number = input("Enter mobile number: ")
        Contact(f_name, l_name, address, city, state, pincode, email, mobile_number)