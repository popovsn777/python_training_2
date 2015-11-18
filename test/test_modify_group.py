__author__ = 'popov.sn'

from model.group import Group


def test_modify_group_name(app):
    if app.group.count()== 0:
        app.group.create(Group(name="no_test_before"))

    old_groups = app.group.get_group_list()

    app.group.modify_first_group(Group(name="New_group"))

    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)


def test_modify_group_header(app):
    if app.group.count()== 0:
        app.group.create(Group(name="no_test_before"))

    old_groups = app.group.get_group_list()

    app.group.modify_first_group(Group(header="New header"))

    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)
