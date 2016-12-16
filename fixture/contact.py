from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_contact_page(self):
        # return to home page
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def contact_creation(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("nowy wpis").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_contact_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Usuń']").click()
        wd.switch_to_alert().accept()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='nav']//a[.='strona główna']").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_contact_name(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//table[@id ='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact from
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=cells[2].text, id=id))
        return contacts

