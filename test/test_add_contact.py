# -*- coding: utf-8 -*-
import pytest

from fixture.application_for_contact import Application_for_contact
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application_for_contact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session_for_contact.login(username="admin", password="secret")
    app.group_for_contact.contact_creation(Contact( firstname="afadf", middlename="sfgsgf", lastname="sgfsgfdg"))
    app.session_for_contact.logout()




