#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

from abc import ABCMeta, abstractmethod
from qaction import QAction
from qstate import QState


DEFAULT_VALUE = 0.0


class QTable(metaclass=ABCMeta):

    @abstractmethod
    def get_value(self, state: QState, action: QAction) -> float:
        pass

    def get_best_value(self, state: QState) -> float:
        if state is None:
            raise TypeError
        act_vals = self.get_action_values(state)
        return max(act_vals, key=lambda key: act_vals[key])

    def get_action_values(self, state: QState) -> dict:
        if state is None:
            raise TypeError
        stored_act_vals = self.get_stored_action_values(state)
        actions = state.get_available_actions()
        return dict([(a, stored_act_vals.get(a, DEFAULT_VALUE)) for a in actions ])

    def get_action_values_as_string(self, state: QState) -> str:
        if state is None:
            raise TypeError
        return ', '.join(['[{}:{}]'.format(k, v) for (k, v) in
                          sorted(self.get_action_values(state).items(), key=lambda x: x[0])
                          ])

    @abstractmethod
    def get_stored_action_values(self, state: QState) -> dict:
        pass
