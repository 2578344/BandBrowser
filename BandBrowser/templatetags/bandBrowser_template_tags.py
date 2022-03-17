from django import template
from BandBrowser.models import UserProfile

register = template.Library()

def get_category_list():
    return {'users': UserProfile.objects.all()}
