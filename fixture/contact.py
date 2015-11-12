__author__ = 'popov.sn'

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.addres)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        #select first contact
#        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_name("selected[]").click()
        #submit "delete"
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
#        wd.find_element_by_value("Delete").click()
        #commit deletion
        wd.switch_to_alert().accept()



    def open_contact_page(self):
        # adding new contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
