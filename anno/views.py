#coding=utf8

from django.shortcuts import render
from django.http import HttpResponse
import datetime
from Utils.SearchResultHub import SearchResultHub
from Utils import LogParser
from django.template import loader
from django import template
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction, models

import sys
import urllib
from anno.models import Task
reload(sys)
def hello(request):
    return HttpResponse('hello world')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def search(request,taskid,query,pageid):

    print 'view search', query
    srh = SearchResultHub()
    query = urllib.unquote(query)

   # query = query.decode('cp936','ignore').decode('utf8')

    # print urllib.quote(query)
    results = srh.getResult(query, 10*(int(pageid)-1), 10)
    results_count = srh.getCount(query)
    max_pageid = results_count / 10

    t = template.Template(open('templates/out.html').read())
    next_pageid = ''
    if int(pageid) < max_pageid:
        next_pageid = str(int(pageid)+1)
    page_str = ''.join([str(x) for x in range(1, max_pageid+1)])
    c = template.Context({'resultlist': [r.content for r in results],
                          'taskid': taskid,
                          'query': query,
                          'pageid': pageid,
                          'page_str': page_str,
                          'next_pageid': next_pageid})
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

def login(request):
    return HttpResponse(open('templates/login.html').read())

def tasks(request,sID):
    tlist = Task.objects.all()
    print 'len tlist',len(tlist)
    for t in tlist:
        print t.task_id
        print t.content
    html = template.Template(open('templates/tasks.html').read())


    c = template.Context({'tasks':tlist,})


    respon = HttpResponse(html.render(c))
    respon.set_cookie('studentID', value=sID, max_age=None, expires=None, path='/', domain=None, secure=None)
    return respon


@csrf_exempt
def log(request):
    message = urllib.unquote(request.POST[u'message'])
    #now I just print the log info for debugging
    LogParser.insertMessageToDB(message)
    return HttpResponse('OK')
