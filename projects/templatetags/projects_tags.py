from django import template
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy

from vote.models import UP, DOWN

register = template.Library()

@register.simple_tag
def member_of(user, legal_entity_pk):
    return user.is_authenticated and user.member_of(legal_entity_pk)

@register.simple_tag
def vote_exists(report, user_pk):
    return report.votes.exists(user_pk, action=UP) or report.votes.exists(user_pk, action=DOWN)

@register.filter
def leva(value):
    if value == 0:
        return '0 ' + _('lv')

    if value is None:
        return _("unknown")

    return "%.2f " % value + _('lv') 


STATUS_COLOR = {
    'review': 'warning',
    'delivered': 'success',
    'accepted': 'default',
    'declined': 'danger',
    }

@register.filter
def status_color(status):
    return STATUS_COLOR.get(status, 'default')

@register.filter
def status_text(status):
    return gettext_lazy(status)
