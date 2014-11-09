__author__ = 'cheng'
from Utils.Question import Question


class ChooseQuestion(Question):
    def __init__(self, desc, items, rightanswer):
        self.desc = desc
        self.items = list()
        for item in items:
            self.items.append(item)
        self.rightanswer = rightanswer

        self.qtype = 'choose'


