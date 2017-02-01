from model.contact import Contact
import random


def test_modify_first_contact(app, db):

    if db.get_contact_list == 0:
        app.contact.contact_creation((Contact(firstname="test"))
    old_contacts = db.get_contact_list
        old_contact = random.choice(old_contacts)
    contact = Contact(firstname="New name")
    contact.id = old_contact.id
    app.contact.modify_contact_by_id(old_contact.id, contact)
    new_contacts = db.get_contact_list
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#def test_modify_contact_name(app):
#    if app.contact.count() == 0:
#        app.contact.contact_creation(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    index = randrange(len(old_contacts))
#    contact = Contact(firstname="New name")
#    contact.id = old_contacts[index].id
#    app.contact.modify_contact_by_index(index, contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[index] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


