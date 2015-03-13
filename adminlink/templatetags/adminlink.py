from django import template
from django.contrib.admin import site
from django.contrib.admin.sites import AlreadyRegistered
from django.core.urlresolvers import reverse


register = template.Library()

@register.simple_tag(takes_context=True)
def adminlink(context, model):
    request = context['request']
    if request.user.is_staff:
        klass = model.__class__
        try:
            site.register(klass)
        except AlreadyRegistered:
            url_name = 'admin:%s_%s_change' % (klass._meta.app_label, klass._meta.object_name.lower())
            link = '<a href="%s" target="_blank">View in admin</a>' % reverse(url_name, args=(model.id,))
            return link
    return ''
