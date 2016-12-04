
class GroupHelperModifyContact:

    def __init__(self, app):
        self.app = app

    def modify_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("grupy").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Edytuj grupę']").click()
        wd.find_element_by_xpath("//input[@value='Aktualizuj']").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()