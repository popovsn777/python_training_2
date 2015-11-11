# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group


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


    
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group( Group(name="new_group_name2", header="group_header2", footer="group_footer2"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

