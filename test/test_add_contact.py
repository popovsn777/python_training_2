__author__ = 'popov.sn'

import pytest
from fixture.application import Application
from model.contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact(Contact(name ="new_fst_name", lastname="new_contact_lst_name", addres="Moscow"))
    app.session.logout()


