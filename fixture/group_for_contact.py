
class GroupHelperContact:

    def __init__(self, app):
        self.app = app

    def return_to_contact_page(self):
        # return to home page
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def contact_creation(self, contact):
        wd = self.app.wd
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

    def delete_first_contact(self):
        wd = self.app.wd
        # select del contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Usuń']").click()
        wd.switch_to_alert().accept()