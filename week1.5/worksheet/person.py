# Worksheet 1.5: Person class
from datetime import datetime as d

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """Initialiser for Person class"""
        self.name = name
        self.birth = birth

        if not type(self.name) is str:
            raise TypeError
        elif not isinstance(birth, d):
            raise TypeError
        elif len(self.name) == 0:
            raise ValueError

    def initials(self):
        """Returns initials of object of person"""
        initialList = ""
        initialList = initialList + self.name[0]
        for i in range(len(self.name)):
            if self.name[i] == " ":
                initialList = initialList + self.name[i+1]
        initialList = initialList.upper()
        return initialList

    def is_birthday(self):
        """If today is the birtday checker"""
        today = d.today()
        if self.birth.strftime("%d") == today.strftime("%d") and self.birth.strftime("%b") == today.strftime("%b"):
            return True
        else:
            return False
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)