from selenium.webdriver.firefox.webdriver import WebDriver
class Application_for_contact:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def logout(self):
        # logout
        wd = self.wd
        wd.find_element_by_link_text("Wyloguj się").click()

    def return_to_contact_page(self):
        # return to home page
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def contact_creation(self, contact):
        wd = self.wd
        # init group creation
        wd.find_element_by_link_text("nowy wpis").click()
        # fill group form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # submit group creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_contact_page()

    def login(self):
        wd = self.wd
        # login
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self):
        wd = self.wd
        # open_home_page
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()