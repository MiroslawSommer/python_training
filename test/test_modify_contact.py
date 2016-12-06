from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_contact_name(Contact(firstname="New name"))
