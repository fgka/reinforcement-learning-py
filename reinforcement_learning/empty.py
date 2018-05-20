#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

from abc import ABCMeta, abstractmethod


class AbstractEmpty(metaclass=ABCMeta):

    @classmethod
    def assert_is_of_type(cls, obj):
        assert isinstance(obj, AbstractEmpty), \
            "Argument of type {} is not an instance of {}" \
            .format(obj.__class__.__name__, AbstractEmpty.__name__)

    @abstractmethod
    def abs_method(self, arg: int) -> None:
        return None
