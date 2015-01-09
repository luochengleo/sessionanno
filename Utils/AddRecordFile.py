__author__ = 'defaultstr'

import os
import random
from anno.models import RecordFile


def importRecordFiles(path):
    for filename in os.listdir(path):
        if len(filename) != 10:
            continue
        try:
            int(filename)
        except ValueError:
            continue
        studentID = filename
        for p in os.listdir(os.path.join(path, studentID)):
            idx = int(p.split('.')[0].split('_')[0])
            task_id = 0
            if p.find('_') == -1:
                random.seed(int(studentID))
                tlist = range(1, 13)
                random.shuffle(tlist)
                task_id = tlist[idx-1]
                new_file_name = '%d_%d.mp3' % (idx, task_id)
                command = 'mv "%s" "%s"' % (os.path.join(path, studentID, p),
                                            os.path.join(path, studentID, new_file_name))
                os.system(command)
            else:
                task_id = int(p.split('.')[0].split('_')[1])

            r = RecordFile(studentID=studentID, task_id=task_id,
                           filepath='/static/record/%s/%d_%d.mp3' % (studentID, idx, task_id))
            r.save()


