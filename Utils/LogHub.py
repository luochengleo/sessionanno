#coding=utf8
__author__ = 'luocheng'
from Utils.LogParser import *
from anno.models import *

class LogHub:
    def __init__(self):
        pass

    def getQueriesWithSIDandTaskID(self,s,t):
        logs = Log.objects.filter(studentID=s, task_id=t)
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


    def getClickedResults(self, studentID, taskid, query):
        clicked_logs = Log.objects.filter(studentID=studentID,
                                            task_id=taskid,
                                            query=query,
                                            action='CLICK')
        clicked_result_rank = []
        for l in clicked_logs:
            c = l.content
            clicked_result_rank.append(getRankOfClickResult(c))

        return SearchResult.objects.filter(query=query, rank__in=clicked_result_rank)

    def getViewedResults(self, taskid, query, max_num=10):
        goto_page_logs = Log.objects.filter(task_id=taskid, query=query)
        pages = [get_target_page(log) for log in goto_page_logs]
        last_page = max(pages+[1])
        query = Query.objects.filter(content=query)[0]
        num = min(last_page * 10, query.resultnum)
        num = min(num, max_num)
        print num
        sr_list = SearchResult.objects.filter(query=query.content)
        print len(sr_list)
        return sorted(sr_list, key=lambda x:x.rank)[0:num]

