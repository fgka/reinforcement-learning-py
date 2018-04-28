#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

from abc import ABCMeta, abstractmethod


class QAction(metaclass=ABCMeta):

    @classmethod
    def assert_is_of_type(cls, obj):
        assert isinstance(obj, QAction), \
            "Argument of type {} is not an instance of {}" \
            .format(obj.__class__.__name__, QAction.__name__)

    @abstractmethod
    def get_available_actions(self):
        pass

    def __hash__(self):
        return self.hash_code()

    @abstractmethod
    def hash_code(self) -> int:
        pass

    @abstractmethod
    def compare_to(self, other) -> int:
        self.__class__.assert_is_of_type(other)
        return 0

    def __lt__(self, other):
        return 0 > self.compare_to(other)

    def __le__(self, other):
        return 0 >= self.compare_to(other)

    def __eq__(self, other):
        return 0 == self.compare_to(other)

    def __ne__(self, other):
        return 0 != self.compare_to(other)

    def __gt__(self, other):
        return 0 < self.compare_to(other)

    def __ge__(self, other):
        return 0 <= self.compare_to(other)
