__author__ = 'popov.sn'

from model.contact import Contact

def test_del_first_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.add_new_contact(Contact(name ="adding_a_new_contact" ))
    app.contact.delete_first_contact()
