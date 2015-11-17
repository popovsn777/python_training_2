# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create( Group(name="new_group_name2", header="group_header2", footer="group_footer2"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


