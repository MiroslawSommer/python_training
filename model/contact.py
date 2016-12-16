

class Contact:
    def __init__(self, firstname=None, lastname=None, middlename=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname
