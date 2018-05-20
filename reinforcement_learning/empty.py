#!/usr/bin/env python
# vim: ai:sw=4:ts=4:sta:et:fo=croql
# coding=utf-8

from abc import ABCMeta, abstractmethod


class AbstractEmpty(metaclass=ABCMeta):

    @abstractmethod
    def abs_method(self, arg: int) -> None:
        return None