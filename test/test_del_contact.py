


def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.group_for_contact.delete_first_contact()
    app.session.logout()