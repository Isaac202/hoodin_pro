from django.contrib.admin.widgets import AutocompleteMixin
from django.urls import reverse

class AutoComplete(AutocompleteMixin):

    def __init__(self, rel, admin_site, attrs=None, choices=(), using=None):
            self.rel = rel
            self.admin_site = admin_site
            self.db = using
            self.choices = choices
            self.attrs = {} if attrs is None else attrs.copy()
     
    def get_url(self):
        model = self.rel.model
        return reverse(self.url_name % (self.admin_site.name, model._meta.app_label, model._meta.model_name))
