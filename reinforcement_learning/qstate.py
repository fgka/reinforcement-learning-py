#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

from abc import ABCMeta, abstractmethod


class QState(metaclass=ABCMeta):

    @classmethod
    def assert_is_of_type(cls, obj):
        assert isinstance(obj, QState), \
            "Argument of type {} is not an instance of {}" \
            .format(obj.__class__.__name__, QState.__name__)

    @abstractmethod
    def get_available_actions(self) -> list:
        pass

    def __hash__(self):
        return self.hash_code()

    @abstractmethod
    def hash_code(self) -> int:
        pass

    def __eq__(self, other):
        return self.equals(other)

    def __ne__(self, other):
        return not self.equals(other)

    @abstractmethod
    def equals(self, other) -> bool:
        QState.assert_is_of_type(other)
