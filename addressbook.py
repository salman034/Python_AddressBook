# Ability to create a Contacts in Address Book with first and last names, address,
# city, state, zip, phone number and email...

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

        print(self.first_name, self.last_name, self.address, self.city, self.state, self.pin_code, self.email_id, self.mobile_number)


if __name__ == "__main__":
    print("Welcome to address book")
    Contact('Salman|', 'Pasha|', 'BTM 1st stage|', 'Bangalore|', 'Karnataka |', '560029 |', 'mkspasha@gmail.com |', '9845715264')