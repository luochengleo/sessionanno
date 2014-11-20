#coding=utf8

from django.shortcuts import render
from django.http import HttpResponse
import datetime
from Utils.SearchResultHub import SearchResultHub
from django.template import loader
from django import template

import sys
import urllib
reload(sys)
from django.template import Template
def hello(request):
    return HttpResponse('hello world')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def search(request,taskid,query,pageid):
    print 'view search',query
    srh = SearchResultHub()
    query = urllib.unquote(query)
    print 'view search after unquote',query

    # query = query.decode('cp936','ignore').decode('utf8')
    print 'after decode',query

    # print urllib.quote(query)
    results = srh.getResult(query,10*int(pageid)+1,10)

    t = Template(open('templates/out.html').read())
    c = template.Context({'resultlist': [r.content for r in results]})
    # fout = open('temp/test.html','w')
    # fout.write(t.render(c).decode('utf8','ignore').encode('utf8'))
    # fout.close()
    return HttpResponse(t.render(c))

def train(request,userid):
    html = '<html><body> It is the '+userid +' train task </body></html>'
    return HttpResponse(html)
def validate(request,taskid):
    html = '<html><body> It is the '+taskid +' task. </body></html>'
    return HttpResponse(html)