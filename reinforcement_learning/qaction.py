#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8
""" .. py:currentmodule:: qaction

Abstract definition of :py:class:`QAction`.
"""

from abc import ABCMeta, abstractmethod


class QAction(metaclass=ABCMeta):
    """Subclasses implement domain-specific \
        (for a particular world and experiment) \
        actions that need to be hashable.

    Actions need to be comparable to maintain a fixed order.
    """

    @classmethod
    def assert_is_of_type(cls, obj):
        """To be used when validating a given argument/variable \
            is an instance of :py:class:`QAction`.
        Usage::

            QAction.assert_is_of_type(action)

        :param object obj: Object to be test if it is a proper \
            instance of :py:class:`QAction`
        :raises AssertionError: if argument is not an instance of \
            :py:class:`QAction`
        """
        assert isinstance(obj, QAction), \
            "Argument of type {} is not an instance of {}" \
            .format(obj.__class__.__name__, QAction.__name__)

    def __hash__(self):
        return self.hash_code()

    @abstractmethod
    def hash_code(self) -> int:
        """Ought to be implement to return a content stable ``int``.

        This method is used inside the :py:meth:`__hash__` \
            and is here to force its implementation.

        :return: the content aware hash code
        :rtype: int
        """
        pass

    @abstractmethod
    def compare_to(self, other) -> int:
        """Must work similar to Java ``Comparator``, i.e., \
            the return value complies with:

        * ``=0`` if :py:class:`QAction` instances are semantically equivalent
        * ``<0`` if this instance should come **before** the argument ``other``
        * ``>0`` if this instance should come **after** the argument ``other``

        :param object other: instance of :py:class:`QAction` to compare to
        :return: a ``Comparator`` equivalent value
        :rtype: int
        """
        QAction.assert_is_of_type(other)
        return 0

    def __lt__(self, other):
        return self.compare_to(other) < 0

    def __le__(self, other):
        return self.compare_to(other) <= 0

    def __eq__(self, other):
        return self.compare_to(other) == 0

    def __ne__(self, other):
        return self.compare_to(other) != 0

    def __gt__(self, other):
        return self.compare_to(other) > 0

    def __ge__(self, other):
        return self.compare_to(other) >= 0
