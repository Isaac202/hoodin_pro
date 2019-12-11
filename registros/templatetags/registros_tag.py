from django import template

register = template.Library()

from django.db.models import Count
# >>> pubs = Publisher.objects.annotate(num_books=Count('book'))


