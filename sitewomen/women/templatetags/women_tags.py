from django import template
from women.models import Category, TagPost
import women.views as views


register = template.Library()


# @register.simple_tag(name='getcats')
# def get_categories():
#     return views.cats_db
#

@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.all()}
