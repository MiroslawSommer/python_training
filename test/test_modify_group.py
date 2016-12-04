

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group_modify.modify_first_group()
    app.session.logout()