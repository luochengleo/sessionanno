#coding=utf8
__author__ = 'cheng'

from anno.models import *
from Utils.SearchResultCrawler import SearchResultCrawler
from Utils.SearchResultPageParser import SearchResultPageParser
from bs4 import BeautifulSoup

import time


class SearchResultHub:
    def __init__(self):
        pass

    def getResult(self, query, beginIndex, number):

        print 'searching in database'

        queries = Query.objects.filter(content=query)

        if len(queries) ==0:
            q = Query(content=query,resultnum=0,recomm='',lastcrawledpage=0)
        else:
            q = queries[0]

        src = SearchResultCrawler()
        srpp = SearchResultPageParser()
        results = list()

        crawlIndex =q.lastcrawledpage+1
        resultnum = q.resultnum


        while resultnum < beginIndex + number:
            content = src.crawl(query, crawlIndex)
            for r in srpp.parse(content):
                soup = BeautifulSoup(r,from_encoding='utf8').find('div', class_='rb')
                if soup.has_attr('id'):
                    soup['id'] = 'rb_'+str(resultnum)
                    robj = SearchResult(query=query, rank=resultnum, result_id='rb_'+str(resultnum), content=str(soup))
                    robj.save()
                    resultnum +=1
                else:
                    print "THE RESULT IS NOT VALID",resultnum
            crawlIndex +=1

        q.resultnum = resultnum
        # TODO recheck  the lastcrawledpage
        q.lastcrawledpage =  crawlIndex -1

        q.save()

        sr_list = SearchResult.objects.filter(query=query)
        return sorted(sr_list, key=lambda x:x.rank)[beginIndex:beginIndex+number]







    def getCount(self, query):
        # sr_list = SearchResult.objects.filter(query=query)
        # modified by luocheng;

        return 90
        # return min(len(sr_list), 90)



    def test(self):
        for item in self.getResult(query='清华大学',beginIndex=1,number=10):
            print '--------------------'
            print item.rank
            print '--------------------'











