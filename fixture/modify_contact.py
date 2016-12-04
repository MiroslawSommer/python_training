class GroupHelperModifyContact:

    def __init__(self, app):
        self.app = app

    def modify_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("strona główna").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("img='icons/pencil.png'").click()
        wd.find_element_by_xpath("//input[@value='Aktualizuj']").click()
        self.return_to_home_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()