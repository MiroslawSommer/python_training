
import pytest
from fixture.application import Application
from fixture.application_for_contact import Application_for_contact

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture()
def app(request):
    fixture = Application_for_contact()
    request.addfinalizer(fixture.destroy)
    return fixture