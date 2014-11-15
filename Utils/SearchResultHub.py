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
            results = list()
            for







