__author__ = 'popov.sn'

from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.contact_count() == 0:
        app.contact.add_new_contact(Contact(name ="adding_a_new_contact" ))
    app.contact.modify_first_contact(Contact(name ="new_fst_name1"))



def test_modify_contact_addres(app):
    if app.contact.contact_count() == 0:
        app.contact.add_new_contact(Contact(name ="adding_a_new_contact" ))
    app.contact.modify_first_contact(Contact(addres ="Tula-la-la"))
