__author__ = 'cheng'

from anno.models import *
from Utils.SearchResultCrawler import SearchResultCrawler
from Utils.SearchResultPageParser import SearchResultPageParser


class SearchResultHub:
    def __init__():
        pass

    def getResult(self, query, beginIndex, number):
        sr_list = SearchResult.objects.filter(query=query)
        if len(sr_list) > 0:
            if beginIndex + number < len(sr_list):
                return sr_list[beginIndex, beginIndex + number]
            else:
                return []
        else:
            src = SearchResultCrawler()
            srpp = SearchResultPageParser()
            results = list()
            for page in range(1, 11, 1):
                for r in srpp.parse(src.crawl(query, page)):
                    results.append(r)
            count = 0
            for r in results:









