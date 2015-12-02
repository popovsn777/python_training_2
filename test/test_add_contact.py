__author__ = 'popov.sn'

from model.contact import Contact



def test_add_new_contact(app):
    print("Debug STEP0")
    old_contacts = app.contact.get_contact_list()
    print("Debug STEP1")
    app.contact.add_new_contact(Contact(name ="new_fst_name3", lastname="new_contact_lst_name3", addres="Moscow3"))
    print("Debug STEP2")
    new_contacts = app.contact.get_contact_list1()
    print("Debug STEP3")
    assert len(old_contacts) + 1 == len(new_contacts)


