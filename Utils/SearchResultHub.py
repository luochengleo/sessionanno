#coding=utf8
__author__ = 'cheng'

from anno.models import *
from Utils.SearchResultCrawler import SearchResultCrawler
from Utils.SearchResultPageParser import SearchResultPageParser
from bs4 import BeautifulSoup

class SearchResultHub:
    def __init__(self):
        pass

    def getResult(self, query, beginIndex, number):
        print 'searching in database'

        sr_list = SearchResult.objects.filter(query=query)
        print len(sr_list)

        if len(sr_list) > 0:
            if beginIndex + number < len(sr_list):
                return sr_list[beginIndex: beginIndex + number]
            else:
                return sr_list[beginIndex:]
        else:
            src = SearchResultCrawler()
            srpp = SearchResultPageParser()
            results = list()
            for page in range(1, 3, 1):
                print 'crawling page', page
                for r in srpp.parse(src.crawl(query, page)):
                    results.append(r)
            count = 0
            for r in results:
                soup = BeautifulSoup(r, from_encoding='utf8').find('div', class_='rb')
                if soup.has_attr('id'):
                    soup['id'] = 'rb_'+str(count)
                    robj = SearchResult(query=query, rank=count, content=str(soup))
                    robj.save()
                    count += 1
                else:
                    print 'do not have key id'
            if len(results) > 0:
                return self.getResult(query, beginIndex, number)
            else:
                #if there is no match, just return empty list
                return []




    def getCount(self, query):
        sr_list = SearchResult.objects.filter(query=query)
        return min(len(sr_list), 90)



    def test(self):
        for item in self.getResult(query='清华大学',beginIndex=1,number=10):
            print '--------------------'
            print item.rank
            print '--------------------'











