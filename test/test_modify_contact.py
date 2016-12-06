from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.contact_creation(Contact(firstname="test"))
    app.contact.modify_contact_name(Contact(firstname="New name"))
