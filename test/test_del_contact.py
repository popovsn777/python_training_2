__author__ = 'popov.sn'


__author__ = 'popov.sn'

def test_del_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()