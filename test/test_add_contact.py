__author__ = 'popov.sn'

from model.contact import Contact



def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact(Contact(name ="new_fst_name1", lastname="new_contact_lst_name1", addres="Moscow1"))
    app.session.logout()


