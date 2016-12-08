from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.contact_creation(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_contact_name(Contact(firstname="New name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
