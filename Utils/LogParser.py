#coding=utf8
__author__ = 'defaultstr'
from anno.models import *
from collections import namedtuple
from django.db import transaction, models
from django.db.models import Q

import re


patterns = {key: re.compile('%s=(.*?)\\t' % key) for key in ['TIME', 'USER', 'TASK', 'QUERY', 'ACTION']}
info_patterns = re.compile('INFO:\\t(.*?)$')
click_info_patterns = {key: re.compile('%s=(.*?)\\t' % key) for key in ['type', 'result', 'page', 'rank']}
click_info_patterns['src'] = re.compile('src=(.*?)$')

SUBJECTS = set(
    ("2013011392\n"
     "2014012991\n"
     "2014011004\n"
     "2011011268\n"
     "2011010412\n"
     "2013010775\n"
     "2014010728\n"
     "2013011395\n"
     "2014620840\n"
     "2013011103\n"
     "2014012337\n"
     "2014010219\n"
     "2014012173\n"
     "2013011400\n"
     "2013012946\n"
     "2011011235\n"
     "2011011239\n"
     "2011011254\n"
     "2013011429\n"
     "2013012949\n"
     "2014013409\n"
     "2012012731\n"
     "2013011437\n"
     "2013013014\n"
     "2014013072\n"
     "2013010773\n"
     "2012011297\n"
     "2014013076\n"
     "2011012703"
    ).split('\n'))




def fromString(line):
    studentID = patterns['USER'].search(line).group(1)
    task_id = patterns['TASK'].search(line).group(1)
    query = patterns['QUERY'].search(line).group(1)
    action = patterns['ACTION'].search(line).group(1)
    logObj = Log.objects.create(studentID=studentID,
                                task_id=task_id,
                                query=query,
                                action=action,
                                content=line)
    return logObj


def getRankOfClickResult(line):
    info = info_patterns.search(line).group(1)
    page = int(click_info_patterns['page'].search(info).group(1))
    rank = int(click_info_patterns['rank'].search(info).group(1))
    print (page-1)*10 + rank
    return (page-1)*10 + rank


def get_queries(users=None):
    logs = Log.objects.filter(Q(action='BEGIN_SEARCH') | Q(action='GOTO_PAGE'))
    page = 1
    results = []
    if users is None:
        users = SUBJECTS
    for log in logs:
        if log.studentID == '2013310564' or log.studentID == '0':
            continue
        if log.studentID not in users:
            continue
        if log.action == 'GOTO_PAGE':
            info = info_patterns.search(log.content).group(1)
            src_page = re.search(r'FROM=sogou_page_(\d{1,2})', info).group(1)
            target_page = re.search('TO=(.*?)$', info).group(1)
            src_page = int(src_page)
            if target_page == 'sogou_next':
                target_page = src_page + 1
            else:
                target_page = int(re.search(r'sogou_page_(\d{1,2})', target_page).group(1))
            page = target_page
        elif log.action == 'BEGIN_SEARCH':
            result = {}
            result['studentID'] = log.studentID
            result['task_id'] = log.task_id
            result['query'] = log.query
            result['page'] = page
            results.append(result)
            page = 1
    return results


def get_target_page(log):
    if log.action != 'GOTO_PAGE':
        return -1
    info = info_patterns.search(log.content).group(1)
    src_page = re.search(r'FROM=sogou_page_(\d{1,2})', info).group(1)
    target_page = re.search('TO=(.*?)$', info).group(1)
    src_page = int(src_page)
    if target_page == 'sogou_next':
        target_page = src_page + 1
    else:
        target_page = int(re.search(r'sogou_page_(\d{1,2})', target_page).group(1))
    return target_page



@transaction.commit_manually
def insertMessageToDB(message):
    try:
        for line in message.split('\n'):
            print line
            if line == '':
                continue
            log = fromString(line)
            log.save()
    except Exception:
        transaction.rollback()
    else:
        transaction.commit()

if __name__ == "__main__":
    import sys
    import os
    sys.path.insert(1, os.path.join(sys.path[0], '..'))
    for line in open('tmp', 'r'):
        print fromString(line)

