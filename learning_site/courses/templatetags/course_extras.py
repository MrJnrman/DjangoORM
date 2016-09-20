from django import template
from django.utils.safestring import mark_safe

import markdown2

from courses.models import Course

'''creating of custom filters and inclusion tags'''
register = template.Library() 

@register.simple_tag
def newest_course():
    '''Gets the most recent published course that was added to the library'''
    return Course.objects.filter(published=True).latest('created_at')


@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list(): 
    '''Returns dictionary of courses to display as navigation pane'''
    # courses = Course.objects.filter(published=True).values('id', 'title')[:5]  # returns the exact fields needed instead of entire dictionary representation, returns first 5
    courses = Course.objects.filter(published=True).order_by('-created_at').values('id', 'title')[:5]  # returns the last 5 created courses
    return {'courses': courses}


@register.filter('time_estimate')
def time_estimate(word_count):
    '''Estimates the number of minutes it will take to complete a step
    based on the passed-in wordcount.
    '''
    minutes = round(word_count/20)
    return minutes


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to HTML'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)