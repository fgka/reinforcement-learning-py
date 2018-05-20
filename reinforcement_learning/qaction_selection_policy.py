#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

from abc import ABCMeta, abstractmethod
from .qaction import QAction


class QActionSelectionPolicy(metaclass=ABCMeta):

    @classmethod
    def assert_is_of_type(cls, obj):
        assert isinstance(obj, QActionSelectionPolicy), \
            "Argument of type {} is not an instance of {}" \
            .format(obj.__class__.__name__, QActionSelectionPolicy.__name__)

    @abstractmethod
    def select(self, action_values: dict) -> QAction:
        return None
