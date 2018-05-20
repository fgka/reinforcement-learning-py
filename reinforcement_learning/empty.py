#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8
""" .. py:currentmodule:: empty

Abstract definition of :py:class:`AbstractEmpty`.
"""

from abc import ABCMeta, abstractmethod


class AbstractEmpty(metaclass=ABCMeta):
    """TODO add class documentation"""

    @classmethod
    def assert_is_of_type(cls, obj):
        """To be used when validating a given argument/variable \
            is an instance of :py:class:`AbstractEmpty`.
        Usage::

            AbstractEmpty.assert_is_of_type(action)

        :param object obj: Object to be test if it is a proper \
            instance of :py:class:`AbstractEmpty`
        :raises AssertionError: if argument is not an instance of \
            :py:class:`AbstractEmpty`
        """
        assert isinstance(obj, AbstractEmpty), \
            "Argument of type {} is not an instance of {}" \
            .format(obj.__class__.__name__, AbstractEmpty.__name__)

    @abstractmethod
    def abs_method(self, arg: int) -> None:
        """TODO implement and document

        :param int arg: an argument
        :return: something
        :rtype: None
        """
        return None
