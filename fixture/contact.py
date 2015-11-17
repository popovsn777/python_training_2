__author__ = 'popov.sn'

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact):
        wd = self.app.wd
        self.go_to_new_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_value("firstname", contact.name)
        self.change_value("lastname", contact.lastname)
        self.change_value("address", contact.addres)


    def change_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        #select first contact
#        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_name("selected[]").click()
        #submit "delete"
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
#           wd.find_element_by_value("Delete").click()
        #commit deletion
        wd.switch_to_alert().accept()



    def go_to_new_contact_page(self):
        # adding new contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def contact_count(self):
        wd = self.app.wd
        print("contact_Debug1")
        print(len(wd.find_elements_by_name("selected[]")))
        print("contact_Debug2")

        return len(wd.find_elements_by_name("selected[]"))
