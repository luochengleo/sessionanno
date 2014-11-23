#coding=utf8
__author__ = 'luocheng'
from anno.models import Log
from Utils.LogParser import fromString

class LogHub:
    def __init__(self):
        pass
    def getQueriesWithSIDandTaskID(self,s,t):
        logs = Log.objects.filter(studentID=s,task_id=t)
        print 'log hub find log',len(logs)
        alreadyin = set()
        rtr = list()
        for l in logs:
            q  =l.query
            if q in alreadyin:
                pass
            else:
                alreadyin.add(q)
                rtr.append(q)
        return rtr

