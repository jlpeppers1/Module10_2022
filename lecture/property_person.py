
class PropertyPerson:

    def __init__(self, name=''):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if value.isdigit():
            raise ValueError
        self._name = value


##driver
if __name__ == '__main__':
    person1 = PropertyPerson('Michelle')
    try:
        person2 = PropertyPerson('7')
    except ValueError:
        print('Invalid name!')
