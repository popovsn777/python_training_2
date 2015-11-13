__author__ = 'popov.sn'


from model.contact import Contact



def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(name ="new_fst_name1"))
    app.session.logout()


#def test_modify_contact_addres(app):
#    app.session.login(username="admin", password="secret")
#    app.contact.modify_first_contact(Contact(addres ="Tula-la-la"))
#    app.session.logout()