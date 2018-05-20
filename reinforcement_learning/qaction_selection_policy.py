#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8
""" .. py:currentmodule:: qaction_selection_policy

Abstract definition of :py:class:`QActionSelectionPolicy`.
"""

from abc import ABCMeta, abstractmethod
from .qaction import QAction


class QActionSelectionPolicy(metaclass=ABCMeta):
    """Defines the shape of an action selection policy used in the \
        :py:meth:`QLearningAlgorithm.selectAction` method.
    """

    @classmethod
    def assert_is_of_type(cls, obj):
        """To be used when validating a given argument/variable \
            is an instance of :py:class:`QActionSelectionPolicy`.
        Usage::

            QActionSelectionPolicy.assert_is_of_type(action)

        :param object obj: Object to be test if it is a proper \
            instance of :py:class:`QActionSelectionPolicy`
        :raises AssertionError: if argument is not an instance of \
            :py:class:`QActionSelectionPolicy`
        """
        assert isinstance(obj, QActionSelectionPolicy), \
            "Argument of type {} is not an instance of {}" \
            .format(obj.__class__.__name__, QActionSelectionPolicy.__name__)

    @abstractmethod
    def select(self, action_values: dict) -> QAction:
        """Returns the action the implemented policy sees fit.
        See each implementation class for the specific strategy.

        :param dict action_values: the available actions, with their values, \
            to select from.
        :return: the action :py:class:`QAction` chosen by the policy
        :rtype: :py:class:`QAction`
        """
        return None
