#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

from abc import ABCMeta, abstractmethod


class QAction(metaclass=ABCMeta):

    @abstractmethod
    def get_available_actions(self):
        pass

    def __hash__(self):
        return self.hash_code()

    @abstractmethod
    def hash_code(self) -> object:
        pass

    @abstractmethod
    def compareTo(self, other: QAction) -> int:
        pass

    def __lt__(self, other):
        return 0 > self.compareTo(other)

    def __le__(self, other):
        return 0 >= self.compareTo(other)

    def __eq__(self, other):
        return 0 == self.compareTo(other)

    def __ne__(self, other):
        return 0 != self.compareTo(other)

    def __gt__(self, other):
        return 0 < self.compareTo(other)

    def __ge__(self, other):
        return 0 <= self.compareTo(other)
