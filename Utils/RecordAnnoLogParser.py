#coding=utf8
__author__ = 'defaultstr'
from anno.models import *
from django.db import transaction, models
import urllib
import re


patterns = {key: re.compile('%s=(.*?)\\t' % key) for key in ['annotatorID', 'studentID', 'task_id']}
patterns['score'] = re.compile('score=(.*?)$')


def fromString(line):
    annotatorID = patterns['annotatorID'].search(line).group(1)
    studentID = patterns['studentID'].search(line).group(1)
    task_id = patterns['task_id'].search(line).group(1)
    score = patterns['score'].search(line).group(1)
    log_obj = RecordAnnotation.objects.create(annotatorID=annotatorID,
                                              studentID=studentID,
                                              task_id=int(task_id),
                                              score=float(score))
    print log_obj
    return log_obj


@transaction.commit_manually
def insertMessageToDB(message):
    try:
        for line in message.split('\n'):
            #print line
            if line == '':
                continue
            log = fromString(line)
            log.save()
    except Exception:
        print 'rollback!'
        transaction.rollback()
    else:
        print "commit success!"
        transaction.commit()
