# coding=utf8
__author__ = 'cheng'

from Utils.Question import Question


class FillingQuesiton(Question):
    def __int__(self, desc):
        self.desc = desc
        self.qtype = 'filling'