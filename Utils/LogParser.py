#coding=utf8
__author__ = 'defaultstr'
from anno.models import *
from django.db import transaction, models
import re




def fromString(line):
    patterns = {key: re.compile('%s=(.*?)\\t' % key) for key in ['TIME', 'USER', 'TASK', 'QUERY', 'ACTION']}
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

@transaction.commit_manually
def insertMessageToDB(message):
    try:
        for line in message.split('\n'):
            print line
            if line == '':
                continue
            log = fromString(line)
            log.save()
    except:
        transaction.rollback()
    else:
        transaction.commit()

if __name__ == "__main__":
    import sys
    import os
    sys.path.insert(1, os.path.join(sys.path[0], '..'))
    for line in open('tmp', 'r'):
        print fromString(line)

