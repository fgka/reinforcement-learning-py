#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

from abc import ABCMeta, abstractmethod
from .qaction import QAction
from .qstate import QState


DEFAULT_VALUE = 0.0


class QTable(metaclass=ABCMeta):

    @classmethod
    def assert_is_of_type(cls, obj):
        assert isinstance(obj, QTable), \
            "Argument of type {} is not an instance of {}" \
            .format(obj.__class__.__name__, QTable.__name__)

    def get_value(self, state: QState, action: QAction) -> float:
        QState.assert_is_of_type(state)
        QAction.assert_is_of_type(action)
        result = DEFAULT_VALUE
        stored = self.get_stored_action_values(state)
        if stored is not None:
            result = stored.get(action, DEFAULT_VALUE)
        return result

    def get_best_value(self, state: QState) -> float:
        QState.assert_is_of_type(state)
        result = DEFAULT_VALUE
        if state is None:
            raise TypeError
        act_vals = self.get_action_values(state)
        if act_vals is not None and len(act_vals) > 0:
            result = act_vals[max(act_vals, key=lambda key: act_vals[key])]
        return result

    def get_action_values(self, state: QState) -> dict:
        QState.assert_is_of_type(state)
        if state is None:
            raise TypeError
        stored_act_vals = self.get_stored_action_values(state)
        if stored_act_vals is None:
            stored_act_vals = {}
        actions = state.get_available_actions()
        return dict([(a, stored_act_vals.get(a, DEFAULT_VALUE))
                     for a in actions])

    def get_action_values_as_string(self, state: QState) -> str:
        QState.assert_is_of_type(state)
        if state is None:
            raise TypeError
        return ', '.join(['[{}:{}]'.format(k, v) for (k, v) in
                          sorted(self.get_action_values(state).items(),
                                 key=lambda x: x[0])])

    @abstractmethod
    def get_stored_action_values(self, state: QState) -> dict:
        QState.assert_is_of_type(state)
        return None
