# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.group_for_contact.contact_creation(Contact( firstname="afadf", middlename="sfgsgf", lastname="sgfsgfdg"))
    app.session.logout()




