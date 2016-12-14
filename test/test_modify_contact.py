from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.contact_creation(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    contact = Contact(firstname="New name")
    app.contact.modify_contact_name(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)