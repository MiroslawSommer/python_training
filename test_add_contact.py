# -*- coding: utf-8 -*-
import pytest
from contact import Contact

from application_for_contact import Application_for_contact


@pytest.fixture
def app(request):
    fixture = Application_for_contact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login()
    app.contact_creation(Contact( firstname="afadf", middlename="sfgsgf", lastname="sgfsgfdg"))
    app.logout()




