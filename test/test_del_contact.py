__author__ = 'popov.sn'

from model.contact import Contact

def test_del_first_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.add_new_contact(Contact(name ="adding_a_new_contact" ))

    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
