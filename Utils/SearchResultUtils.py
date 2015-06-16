__author__ = 'defaultstr'

from anno.models import SearchResult
from anno.models import Task
from LogParser import get_queries
from django import template
from Utils.SearchResultHub import SearchResultHub
from collections import defaultdict
import urllib
import re


def get_all_queries():
    query_set = set()
    for x in get_queries():
        task_id = x['task_id']
        query = x['query']
        query_set.add((task_id, query))
    return query_set


def get_results(query, num=5):
    sr_list = SearchResult.objects.filter(query=query)
    return sorted(sr_list, key=lambda x:x.rank)[0:num]


def filter_scripts(html):
    html = re.sub(r'initEndorseShow2\((.*?)\);', '', html)
    html = html.replace('***', '')
    return html


def get_html_strings(num=5):
    query_set = get_all_queries()
    _id = 0
    res = []
    for task_id, query in query_set:
        task = Task.objects.filter(task_id=int(task_id))[0]
        results = get_results(query, num=num)
        for result in results:
            t = template.Template(open('templates/rel_annotation_static.html').read())
            c = template.Context({'resultlist': [filter_scripts(result.content)],
                                  'task_desc': task.content,
                                  'taskid': task_id,
                                  'query': query})
            html_str = t.render(c)
            print type(html_str)
            print _id
            res.append((result.id, html_str))
            _id += 1
    return res


def output_to_text_file():
    results = get_html_strings(num=5)
    fout = open('./data/top5.txt', 'w')
    for r in results:
        print >>fout, '%d***%s' % (r[0], str(r[1].encode('utf8')).replace('\n', ''))
    fout.close()


def output_to_html_file():
    results = get_html_strings(num=10)
    for r in results:
        fout = open('./data/single_result/%d.html' % r[0], 'w')
        print >>fout, str(r[1].encode('utf8')).replace('\n', '')
        fout.close()


def get_anno_page(taskid, query, pageid):
    srh = SearchResultHub()

    results = srh.getResult(query, 10*(int(pageid)-1), 10)
    results_count = srh.getCount(query)
    max_pageid = results_count / 10

    t = template.Template(open('templates/out_anno_page.html').read())
    next_pageid = ''
    if int(pageid) < max_pageid:
        next_pageid = str(int(pageid)+1)
    page_str = ''.join([str(x) for x in range(1, max_pageid+1)])
    #result_list = SERPAnalyzer.add_character_bounding_box(results)
    result_list = [r.content for r in results]
    task = Task.objects.get(task_id=int(taskid))
    c = template.Context({'resultlist': result_list,
                          'task_desc': task.content,
                          'taskid': taskid,
                          'query': query,
                          'pageid': pageid,
                          'page_str': page_str,
                          'next_pageid': next_pageid})
    # fout = open('temp/test.html','w')
    # fout.write(t.render(c).decode('utf8','ignore').encode('utf8'))
    # fout.close()
    return filter_scripts(t.render(c))


def generate_anno_page_by_task():
    fin = open('data/page_anno/queries.txt', 'r')
    task2html = defaultdict(list)
    task2info = defaultdict(list)

    for idx, line in enumerate(fin):
        print idx
        task, query, scores = line.split('\t')
        task2info[task].append((idx, line.rstrip()))
        html = get_anno_page(task, query, "1")
        task2html[task].append((idx, str(html.encode('utf8')).replace('\n', '')))

        assert len(task2html) == len(task2info)

    for task in task2html:
        fout = open('data/page_anno/%s_info.txt' % task, 'w')
        for idx, info in task2info[task]:
            print >>fout, '%d\t%s' % (idx, info)
        fout = open('data/page_anno/%s_html.txt' % task, 'w')
        for idx, html in task2html[task]:
            print >>fout, '%d***%sGEOGEO 120.0 -40.0 5.0' % (idx, html)
        print >>fout, ''
#output_to_text_file()
#output_to_html_file()
