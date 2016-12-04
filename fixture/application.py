from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group_for_contact import GroupHelperContact
from fixture.session import SessionHelper
from fixture.group_modify_contact import GroupHelperModifyContact
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.group_for_contact = GroupHelperContact(self)
        self.group_modify_contact = GroupHelperModifyContact(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

