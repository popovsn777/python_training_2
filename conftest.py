__author__ = 'popov.sn'

import pytest
from fixture.application import Application


fixture = None

@pytest.fixture
def app(request):
    print ("DEBUG fixture")
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture