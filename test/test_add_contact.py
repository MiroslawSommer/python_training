# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.contact_creation(Contact( firstname="afadf", middlename="sfgsgf", lastname="sgfsgfdg"))





