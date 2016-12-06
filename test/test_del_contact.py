from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.contact_creation(Contact(firstname="test"))
    app.contact.delete_first_contact()
