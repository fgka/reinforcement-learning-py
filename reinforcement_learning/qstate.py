#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

from abc import ABCMeta, abstractmethod


class QState(metaclass=ABCMeta):

    @abstractmethod
    def get_available_actions(self) -> list:
        pass

    def __hash__(self):
        return self.hash_code()

    @abstractmethod
    def hash_code(self) -> object:
        pass

    def __eq__(self, other):
        return self.equals(other)

    @abstractmethod
    def equals(self, other: QState) -> bool:
        pass
