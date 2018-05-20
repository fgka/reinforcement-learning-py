#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

import pytest
# Uncomment to run test in debug mode
# import pudb; pudb.set_trace()

"""
Empty test
"""


def test_ok():
    # given
    # when
    # then
    assert True

@pytest.mark.incremental
class TestEmpty(object):

    # given
    value = True

    def test_ok(self):
        # when
        # then
        assert self.value
