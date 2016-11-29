from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session_for_contact import SessionHelperContact
from fixture.group_for_contact import GroupHelperContact

class Application_for_contact:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session_for_contact = SessionHelperContact(self)
        self.group_for_contact = GroupHelperContact(self)


    def open_home_page(self):
        wd = self.wd
        # open_home_page
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()