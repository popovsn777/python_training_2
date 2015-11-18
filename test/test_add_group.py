# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    print("Debug old_groups = ", len(old_groups) )
    app.group.create( Group(name="new_group_name2", header="group_header2", footer="group_footer2"))
    new_group = app.group.get_group_list()
    print("Debug new_groups = ", len(new_group) )
    assert len(old_groups) + 1 == len(new_group)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_group = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_group)


