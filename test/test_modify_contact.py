from model.contact import Contact

def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_contact_name(Contact( firstname="New name")
    app.session.logout()