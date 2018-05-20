#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8
""" .. py:currentmodule:: qtable

Abstract definition of :py:class:`QTable`.
"""

from abc import ABCMeta, abstractmethod
from .qaction import QAction
from .qstate import QState


DEFAULT_VALUE = 0.0


class QTable(metaclass=ABCMeta):
    """QTable stores the learned *action* :py:class:`QAction` values \
        for a particular *state* :py:class:`QState`.
    """

    @classmethod
    def assert_is_of_type(cls, obj):
        """To be used when validating a given argument/variable \
            is an instance of :py:class:`QTable`.
        Usage::

            QTable.assert_is_of_type(action)

        :param object obj: Object to be test if it is a proper \
            instance of :py:class:`QTable`
        :raises AssertionError: if argument is not an instance of \
            :py:class:`QTable`
        """
        assert isinstance(obj, QTable), \
            "Argument of type {} is not an instance of {}" \
            .format(obj.__class__.__name__, QTable.__name__)

    def get_value(self, state: QState, action: QAction) -> float:
        """Returns the value corresponding to the :py:class:`QAction` in the \
            :py:class:`QState`.

        :param object state: a :py:class:`QState` instance
        :param object action: a :py:class:`QAction` instance
        :return: either the stored value for the pair ``(state, action)`` \
            or :py:const:`DEFAULT_VALUE`
        :rtype: float
        """
        QState.assert_is_of_type(state)
        QAction.assert_is_of_type(action)
        result = DEFAULT_VALUE
        stored = self.get_stored_action_values(state)
        if stored is not None:
            result = stored.get(action, DEFAULT_VALUE)
        return result

    @abstractmethod
    def set_value(self, state: QState, action: QAction, value: float) -> None:
        """Must store the given value \
            for the corresponding pair ``(state, action)``

        :param object state: a :py:class:`QState` instance
        :param object action: a :py:class:`QAction` instance
        :param float value: the corresponding value to be saved
        :rtype: None
        """
        QState.assert_is_of_type(state)
        QAction.assert_is_of_type(action)
        return None

    def get_best_value(self, state: QState) -> float:
        """For a given state returns the best value, \
            across all available actions.

        :param object state: a :py:class:`QState` instance
        :return: the best value found to all avaiable actions
        :rtype: float
        """
        QState.assert_is_of_type(state)
        result = DEFAULT_VALUE
        if state is None:
            raise TypeError
        act_vals = self.get_action_values(state)
        if act_vals is not None and act_vals:
            result = act_vals[max(act_vals, key=lambda key: act_vals[key])]
        return result

    def get_action_values(self, state: QState) -> dict:
        """For a given state returns the best action, \
            i.e, the action with the highest value.

        :param object state: a :py:class:`QState` instance
        :return: the action that has, so far, produced the highest value
        :rtype: :py:class:`QAction`
        """
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
        """Returns a string corresponding to the list of actions \
            for a given state.
        The format is: ``[<action>:<value>]``

        :param object state: a :py:class:`QState` instance
        :return: the string with all pairs ``(action, value)`` for the given \
            state
        :rtype: str
        """
        QState.assert_is_of_type(state)
        if state is None:
            raise TypeError
        return ', '.join(['[{}:{}]'.format(k, v) for (k, v) in
                          sorted(self.get_action_values(state).items(),
                                 key=lambda x: x[0])])

    @abstractmethod
    def get_stored_action_values(self, state: QState) -> dict:
        """For the given state return all stored pairs ``(action, value)`` \
            in a `dict`, where the key is an action :py:class:`QAction` and \
            the value is a `float` corresponding to stored value.

        :param object state: a :py:class:`QState` instance
        :return: a `dict` with all stored ``(action, value)`` for the given \
            state
        :rtype: dict
        """
        QState.assert_is_of_type(state)
        return None

    @abstractmethod
    def get_all_stored_states(self) -> list:
        """Returns a list with all known states.

        :return: all known states :py:class:`QState`
        :rtype: list
        """
        return None

    def __str__(self):
        return '\n'.join([
            '{}->[{}]'.format(
                state,
                ' '.join([
                    '{}:{}'.format(action, value)
                    for action, value in
                    self.get_stored_action_values(state).items()
                ]))
            for state in self.get_all_stored_states()
        ])
