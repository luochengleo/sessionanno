#coding=utf8
__author__ = 'luocheng'

import urllib2
class SearchResultCrawler:
    def __init__(self):
        pass
    def crawl(self,query):
        url ='http://www.sogou.com/web?query='+urllib2.quote(query)+'&num=100'
        webpage = urllib2.urlopen(url).read()
