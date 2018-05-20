#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

import pytest
# Uncomment to run test in debug mode
# import pudb; pudb.set_trace()
from reinforcement_learning.best_action_selection_policy \
    import NON_RANDOM_INSTANCE, RANDOMIZED_INSTANCE
from test_qaction import QActionTest

"""
BestActionSelectionPolicy
"""

TOTAL_ACT_VAL_PAIRS = 20
TOTAL_NON_MAX_PAIRS = 15
TOTAL_MAX_PAIRS = TOTAL_ACT_VAL_PAIRS - TOTAL_NON_MAX_PAIRS
# max value is "fuzzy" to force double proper comparison
MAX_VALUE = 15.1 / 2.7


# given
@pytest.fixture(scope="function")
def action_values(request):
    # create all actions, index can be retrieved through member content
    actions = [QActionTest(i) for i in range(TOTAL_ACT_VAL_PAIRS)]
    # create all non-max values
    values = [float(v) / 3.0 for v in range(TOTAL_NON_MAX_PAIRS)]
    # append the max values to correspond to last actions
    values.extend([MAX_VALUE] * TOTAL_MAX_PAIRS)
    # associate actions to values in value-increasing order
    return dict(zip(actions, values))


def test_non_random(action_values):
    # when
    all_selected = _select_action(action_values, NON_RANDOM_INSTANCE)
    for a in all_selected:
        # then
        assert a.content >= TOTAL_NON_MAX_PAIRS, 'Action: {}'.format(a)
    # regardless which from the max, must always pick the same action
    assert len(all_selected) == 1, 'Actions: {}'.format(all_selected)


def _select_action(action_values, instance, repeat=TOTAL_MAX_PAIRS * 2):
    return set([instance.select(action_values) for i in range(repeat)])


def test_random(action_values):
    # when
    all_selected = _select_action(action_values, RANDOMIZED_INSTANCE)
    for a in all_selected:
        # then
        assert a.content >= TOTAL_NON_MAX_PAIRS, 'Action: {}'.format(a)
    assert len(all_selected) > 1 and len(all_selected) <= TOTAL_MAX_PAIRS, \
        'Actions: {}'.format(all_selected)
