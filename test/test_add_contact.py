__author__ = 'popov.sn'

from model.contact import Contact



def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact(Contact(name ="new_fst_name1", lastname="new_contact_lst_name1", addres="Moscow1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


