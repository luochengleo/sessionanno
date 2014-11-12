from django.test import TestCase
from anno.models import *
# Create your tests here.
if __name__ == '__main__':
    t1 = Task(content='Describe the city you live in', task_id=0)
    t1.save()

