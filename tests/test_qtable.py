#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

import pytest
# Uncomment to run test in debug mode
# import pudb; pudb.set_trace()
from pytest import raises
from reinforcement_learning.qaction import QAction
from reinforcement_learning.qstate import QState
from reinforcement_learning.qtable import QTable, DEFAULT_VALUE
from test_qaction import QActionTest
from test_qstate import QStateTest


"""
QTable
"""


class QTableTest(QTable):

    def __init__(self, stored_action_values: dict):
        self.stored_action_values = stored_action_values

    def set_value(self, state: QState, action: QAction, value: float) -> None:
        return super().set_value(state, action, value)

    def get_stored_action_values(self, state: QState) -> dict:
        return self.stored_action_values.get(state, None)

    def get_all_stored_states(self) -> list:
        return []


def test_is_abstract():
    with raises(TypeError):
        QTable()


def test_assert_is_of_type_fail():
    with raises(AssertionError):
        QTable.assert_is_of_type("")


def test_assert_is_of_type_ok():
    try:
        QTable.assert_is_of_type(QTableTest({}))
        assert True
    except Exception as e:
        assert False, "Should not raise an exception, but got: {}".format(e)


@pytest.mark.incremental
class TestQTable(object):

    # given
    action_a = QActionTest(3)
    action_b = QActionTest(4)
    action_c = QActionTest(5)
    state_a = QStateTest([action_a, action_b])
    state_b = QStateTest([action_c])
    value_a = 123.1
    value_b = 234.5
    state_a_action_values = {
        action_a: value_a,
        action_b: value_b
    }
    stored_action_values = {state_a: state_a_action_values}
    # when
    table = QTableTest(stored_action_values)

    def test_get_value_present(self):
        # then
        assert self.table.get_value(self.state_a, self.action_a) \
            is self.value_a
        assert self.table.get_value(self.state_a, self.action_b) \
            is self.value_b

    def test_get_value_not_present(self):
        # then
        assert self.table.get_value(self.state_a, self.action_c) \
            is DEFAULT_VALUE
        assert self.table.get_value(self.state_b, self.action_a) \
            is DEFAULT_VALUE

    def test_get_action_values_preset(self):
        # then
        result = self.table.get_action_values(self.state_a)
        # should be a copy
        assert result is not self.state_a_action_values
        # check content
        state_actions = self.state_a.get_available_actions()
        assert len(state_actions) == len(result)
        for action in state_actions:
            assert action in result
            assert result[action] == self.state_a_action_values[action]

    def test_get_action_values_not_preset(self):
        # then
        result = self.table.get_action_values(self.state_b)
        state_actions = self.state_b.get_available_actions()
        assert len(state_actions) == len(result)
        for action in state_actions:
            assert action in result
            assert result[action] == DEFAULT_VALUE

    def test_get_best_value_present(self):
        # then
        assert self.table.get_best_value(self.state_a) is self.value_b

    def test_get_best_value_not_present(self):
        # then
        assert self.table.get_best_value(self.state_b) is DEFAULT_VALUE
