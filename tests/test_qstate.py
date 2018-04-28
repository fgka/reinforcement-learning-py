#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

import pytest
from pytest import raises
from reinforcement_learning.qstate import QState
from test_qaction import QActionTest


"""
QState
"""


class QStateTest(QState):

    def __init__(self, content: list):
        self.content = content

    def get_available_actions(self):
        return self.content

    def hash_code(self):
        return hash(frozenset(self.content))

    def equals(self, other):
        super().equals(other)
        return self.content == other.content


def test_is_abstract():
    with raises(TypeError):
        QState()


def test_assert_is_of_type_fail():
    with raises(AssertionError):
        QState.assert_is_of_type("")


def test_assert_is_of_type_ok():
    try:
        QState.assert_is_of_type(QStateTest([]))
        assert True
    except Exception as e:
        assert False, "Should not raise an exception, but got: {}".format(e)


@pytest.mark.incremental
class TestQState(object):

    action_a = QActionTest(1)
    action_b = QActionTest(2)
    action_c = QActionTest(3)
    state_a = QStateTest([action_a, action_b])
    state_b = QStateTest([action_c])
    state_c = QStateTest([action_a, action_b])

    def test__eq_ne__(self):
        assert self.state_a == self.state_a
        assert self.state_a != self.state_b

    def test_hash_code(self):
        qa_to_str = {}
        qa_to_str[self.state_a] = "state_a"
        qa_to_str[self.state_b] = "state_b"
        assert 2 == len(qa_to_str)
        assert "state_a" == qa_to_str[self.state_a]
        # state_a and state_c are semantically equivalent and have same hash
        qa_to_str[self.state_c] = "state_c"
        assert 2 == len(qa_to_str)
        assert "state_c" == qa_to_str[self.state_a]
