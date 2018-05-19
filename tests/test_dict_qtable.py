#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

import pytest
# Uncomment to run test in debug mode
# import pudb; pudb.set_trace()
from reinforcement_learning.dict_qtable import DictQTable
from test_qaction import QActionTest
from test_qstate import QStateTest


"""
DictQTable
"""


@pytest.mark.incremental
class TestDictQTable(object):

    action_a = QActionTest(3)
    action_b = QActionTest(4)
    action_c = QActionTest(5)
    state_a = QStateTest([action_a, action_b])
    state_b = QStateTest([action_c])
    value_a = 123.1
    value_b = 234.5

    def test_set_value(self):
        # given
        obj = DictQTable()
        obj.set_value(self.state_a, self.action_a, self.value_a)
        # when
        stored_states = obj.get_all_stored_states()
        # then
        assert stored_states is not None, 'Table: {}'.format(obj)
        assert len(stored_states) is 1, 'Table: {}'.format(obj)
        assert stored_states[0] is self.state_a, 'Table: {}'.format(obj)
        value = obj.get_value(self.state_a, self.action_a)
        assert value is not None, 'Table: {}'.format(obj)
        assert value is self.value_a, 'Table: {}'.format(obj)

    def test_get_stored_action_values(self):
        # given
        obj = DictQTable()
        obj.set_value(self.state_a, self.action_a, self.value_a)
        obj.set_value(self.state_a, self.action_b, self.value_b)
        # when
        stored_action_values = obj.get_stored_action_values(self.state_a)
        # then
        assert stored_action_values is not None, 'Table: {}'.format(obj)
        assert len(stored_action_values) is 2, 'Table: {}'.format(obj)
        assert self.action_a in stored_action_values.keys(), \
            'Table: {}'.format(obj)
        assert stored_action_values[self.action_a] is self.value_a, \
            'Table: {}'.format(obj)
        assert self.action_b in stored_action_values.keys(), \
            'Table: {}'.format(obj)
        assert stored_action_values[self.action_b] is self.value_b, \
            'Table: {}'.format(obj)
