# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from contact import Contact
import  unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        self.Login(wd, username="admin", password="secret")
        self.add_new_contact(wd, Contact(firstname="asdf", lastname="sdfsf"))
        self.logout(success, wd)

    def logout(self, success, wd):
        # logout
        wd.find_element_by_link_text("Wyloguj się").click()
        self.assertTrue(success)

    def add_new_contact(self, wd, contact):
        # add_new_contact
        wd.find_element_by_link_text("nowy wpis").click()
        #fill contact from
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def Login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
