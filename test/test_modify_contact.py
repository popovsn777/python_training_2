__author__ = 'popov.sn'


from model.contact import Contact


def print_debug(pr_pr):
    print(pr_pr)


def test_modify_contact_name(app):

    print_debug("test!!!!!")
    app.contact.modify_first_contact(Contact(name ="new_fst_name1"))



#def test_modify_contact_addres(app):
#    app.session.login(username="admin", password="secret")
#    app.contact.modify_first_contact(Contact(addres ="Tula-la-la"))
#    app.session.logout()