#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8
""" .. py:currentmodule:: best_action_selection_policy

Definition of :py:class:`BestActionSelectionPolicy`.
"""

import operator
import math
import random
from .qaction import QAction
from .qaction_selection_policy import QActionSelectionPolicy


class BestActionSelectionPolicy(QActionSelectionPolicy):
    '''
    Essentially argmax() if action is viewed as an index into values
    '''

    def __init__(self, randomize):
        super().__init__()
        self._randomize = randomize

    def select(self, action_values: dict) -> QAction:
        result = None
        if action_values is not None and action_values:
            result = self._safe_select(action_values)
        return result

    def _safe_select(self, action_values: dict) -> QAction:
        result = None
        if self._randomize:
            result = _select_random_max(action_values)
        else:
            result = _select_non_random_max(action_values)
        return result


def _select_random_max(action_values: dict) -> QAction:
    max_value = _get_max_value_action_value_pair(action_values)[1]
    return random.choice([action
                          for action, value in action_values.items()
                          if math.isclose(value, max_value)])


def _select_non_random_max(action_values: dict) -> QAction:
    return _get_max_value_action_value_pair(action_values)[0]


def _get_max_value_action_value_pair(action_values: dict) -> tuple:
    return max(action_values.items(), key=operator.itemgetter(1))


# breaks ties randomly
RANDOMIZED_INSTANCE = BestActionSelectionPolicy(True)
# does not break ties, chooses the first
NON_RANDOM_INSTANCE = BestActionSelectionPolicy(False)
DEFAULT_INSTANCE = NON_RANDOM_INSTANCE
