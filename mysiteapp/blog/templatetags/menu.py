from django import template
from django.contrib.auth.models import User

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    user = User.objects.all()
    return {"categories": categories, "menu_class": menu_class, "user": user}
