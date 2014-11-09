#coding=utf8
__author__ = 'luocheng'
import Utils.SearchResultPageParser

import urllib2
class SearchResultCrawler:
    def __init__(self):
        pass
    def crawl(self,query,index=1):
        url ='http://www.sogou.com/web?query='+urllib2.quote(query)+'&num=100&&page='+str(index)+'&ie=utf8'
        try:
            webpage = urllib2.urlopen(url).read()
            return webpage
        except:
            return ''


if __name__ == '__main__':
    src = SearchResultCrawler()
    open('../temp/webpage1.html','w').write(src.crawl('我们的故事',1))
    open('../temp/webpage2.html','w').write(src.crawl('我们的故事',2))
    open('../temp/webpage3.html','w').write(src.crawl('我们的故事',3))
    open('../temp/webpage4.html','w').write(src.crawl('我们的故事',4))
    open('../temp/webpage5.html','w').write(src.crawl('我们的故事',5))

