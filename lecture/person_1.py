
class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''): # Constructor
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def __str__(self):
        if self.address == '':
            return 'Person with last name ' + str(self.last_name) + ', first name ' + str(self.first_name)
        else:
            return 'Person with last name ' + str(self.last_name) + ', first name ' + str(self.first_name) + ' ' +str(self.address)

# Driver
if __name__ == "__main__":
# Valid person
    person1 = Person('Duck', 'Donald', "123 Fake Street\nUrban, Iowa") # ssn not required
    print(str(person1))

    person2 = Person('Duck', 'Donald') # ssn not required
    print(str(person2))
