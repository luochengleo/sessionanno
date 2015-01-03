__author__ = 'defaultstr'
from bs4 import BeautifulSoup


from django import template
register = template.Library()


@register.filter
def add_annotation(value):
    soup = BeautifulSoup(value)
    div = soup.find('div')
    div['style'] = 'float:left; width:550px'
    result_id = div['id']
    t = template.Template(open('templates/result_annotation_template.html').read())
    c = template.Context({'result': str(div), 'id': result_id})
    return t.render(c)