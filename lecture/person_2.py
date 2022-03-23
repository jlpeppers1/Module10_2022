
class PersonTitles:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname, allowed_titles=TITLES):
        if title not in allowed_titles:
            raise ValueError("%s is not a valid title." % title)

        self.title = title
        self._name = name
        self.surname = surname

if __name__ == "__main__":
    try:
        error = PersonTitles("Sir", "John", "Smith")
    except Exception as err:
        print(err)
    person = PersonTitles("Dr", "John", "Smith")

