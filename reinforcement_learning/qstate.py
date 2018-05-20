#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8
""" .. py:currentmodule:: qstate

Abstract definition of :py:class:`QState`.
"""

from abc import ABCMeta, abstractmethod


class QState(metaclass=ABCMeta):
    """Subclasses implement domain-specific \
        (for a particular world and experiment) \
        state that need to be hashable.
    """

    @classmethod
    def assert_is_of_type(cls, obj):
        """To be used when validating a given argument/variable \
            is an instance of :py:class:`QState`.
        Usage::

            QState.assert_is_of_type(action)

        :param object obj: Object to be test if it is a proper \
            instance of :py:class:`QState`
        :raises AssertionError: if argument is not an instance of \
            :py:class:`QState`
        """
        assert isinstance(obj, QState), \
            "Argument of type {} is not an instance of {}" \
            .format(obj.__class__.__name__, QState.__name__)

    @abstractmethod
    def get_available_actions(self) -> list:
        """Returns a list of all available actions \
            (of type :py:class:`QAction`) for this state.

        :return: list of available actions
        :rtype: list
        """
        pass

    def __hash__(self):
        return self.hash_code()

    @abstractmethod
    def hash_code(self) -> int:
        """Ought to be implement to return a content related ``int``.

        This method is used inside the :py:meth:`__hash__` \
            and is here to force its implementation.

        :return: the content aware hash code
        :rtype: int
        """
        pass

    def __eq__(self, other):
        return self.equals(other)

    def __ne__(self, other):
        return not self.equals(other)

    @abstractmethod
    def equals(self, other) -> bool:
        """Ought to be implement to return a content stable ``bool``.

        This method is used inside the :py:meth:`__eq__` \
            and :py:meth:`__ne__` and is here to force its implementation.

        :param object other: an instance of :py:class:`QState`
        :return: the content equivalence
        :rtype: bool
        """
        QState.assert_is_of_type(other)
        return None
