#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

import pytest
# Uncomment to run test in debug mode
# import pudb; pudb.set_trace()
from pytest import raises
from reinforcement_learning.qaction import QAction


"""
QAction
"""


class QActionTest(QAction):

    def __init__(self, content: int):
        self.content = content

    def hash_code(self):
        return self.content.__hash__()

    def compare_to(self, other):
        super().compare_to(other)
        return self.content - other.content


def test_is_abstract():
    with raises(TypeError):
        QAction()


def test_assert_is_of_type_fail():
    with raises(AssertionError):
        QAction.assert_is_of_type("")


def test_assert_is_of_type_ok():
    try:
        # given
        action = QActionTest("")
        # when
        QAction.assert_is_of_type(action)
        # then
        assert True
    except Exception as e:
        assert False, "Should not raise an exception, but got: {}".format(e)


@pytest.mark.incremental
class TestQAction(object):

    # given
    obj_a = QActionTest(1)
    obj_b = QActionTest(2)
    obj_c = QActionTest(1)

    def test__eq_ne___(self):
        # when
        # then
        assert self.obj_a == self.obj_a
        assert self.obj_a != self.obj_b
        assert self.obj_a == self.obj_c

    def test___lt_gt__(self):
        # when
        # then
        assert self.obj_a < self.obj_b
        assert self.obj_b > self.obj_a

    def test___le_ge__(self):
        # when
        # then
        assert self.obj_a <= self.obj_a
        assert self.obj_a >= self.obj_a
        assert self.obj_a <= self.obj_b
        assert self.obj_b >= self.obj_a

    def test_hash_code(self):
        # given
        qa_to_str = {}
        qa_to_str[self.obj_a] = "obj_a"
        qa_to_str[self.obj_b] = "obj_b"
        # when
        assert 2 == len(qa_to_str)
        assert "obj_a" == qa_to_str[self.obj_a]
        # obj_a and obj_c are semantically equivalent and have same hash
        qa_to_str[self.obj_c] = "obj_c"
        # then
        assert 2 == len(qa_to_str)
        assert "obj_c" == qa_to_str[self.obj_a]
