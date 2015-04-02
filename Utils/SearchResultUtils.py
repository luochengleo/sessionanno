__author__ = 'defaultstr'

from anno.models import SearchResult
from anno.models import Task
from LogParser import get_queries
from django import template
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
    return re.sub(r'initEndorseShow2\((.*?)\);', '', html)


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


#output_to_text_file()
output_to_html_file()
