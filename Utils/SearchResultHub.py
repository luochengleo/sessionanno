#coding=utf8
__author__ = 'cheng'

from anno.models import *
from Utils.SearchResultCrawler import SearchResultCrawler
from Utils.SearchResultPageParser import SearchResultPageParser


class SearchResultHub:
    def __init__(self):
        pass

    def getResult(self, query, beginIndex, number):
        print 'searching in database'

        sr_list = SearchResult.objects.filter(query=query)
        print len(sr_list)

        if len(sr_list)>0:
            if (beginIndex + number < len(sr_list)) and (len(sr_list)>100):
                print 'find result'
                return sr_list[beginIndex: beginIndex + number]
            else:
                print  'insufficient results',len(sr_list)-beginIndex
                return sr_list[beginIndex:]

        else:
            print 'begin crawling'
            src = SearchResultCrawler()
            srpp = SearchResultPageParser()
            results = list()
            for page in range(1, 3, 1):
                print 'crawling page', page
                for r in srpp.parse(src.crawl(query, page)):
                    results.append(r)
            count = 0
            print 'find ',len(results) ,' results'
            for r in results:
                count +=1

                robj = SearchResult(query= query, rank = count,content = r)
                print query,count,r
                robj.save()
            return self.getResult(query,beginIndex,number)

    def test(self):
        for item in self.getResult(query='清华大学',beginIndex=1,number=10):
            print '--------------------'
            print item.rank
            print '--------------------'











