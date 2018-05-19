#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

from .qaction import QAction
from .qstate import QState
from .qtable import QTable


class DictQTable(QTable):

    def __init__(self):
        super().__init__()
        self._table = {}

    def set_value(self, state: QState, action: QAction, value: float) -> None:
        super().set_value(state, action, value)
        action_value = self._table.get(state, None)
        if (action_value is None):
            action_value = {}
            self._table[state] = action_value
        action_value[action] = value
        return None

    def get_stored_action_values(self, state: QState) -> dict:
        super().get_stored_action_values(state)
        result = {}
        action_value = self._table.get(state, None)
        if (action_value):
            result = dict(action_value)
        return result

    def get_all_stored_states(self) -> list:
        return [k for k in self._table.keys()]
