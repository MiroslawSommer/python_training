from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, middlename=None, homephone=None, mobilephone=None, workphone=None, seconderyphone=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.seconderyphone = seconderyphone
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(ct):
        if ct.id:
            return int(ct.id)
        else:
            return maxsize