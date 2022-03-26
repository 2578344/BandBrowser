from django import template
from BandBrowser.models import UserProfile
from datetime import datetime
from datetime import timedelta
register = template.Library()

def get_category_list():
    return {'users': UserProfile.objects.all()}

@register.inclusion_tag('BandBrowser/createPostPage.html')
def getUser(user =None):
    userProfile = UserProfile.objects.get_or_create(user=user)[0]
    return {'userProfile': userProfile}

@register.inclusion_tag('BandBrowser/BandInfo.html')
def getBandName(band):
    name = band.slug.replace("-", " ")
    return {'BandName': name}

@register.filter(name='get_class')
def get_class(value):
    return value.__class__.__name__

@register.filter(name='get_Posts')
def get_class(value):
    print(value.post.all())
    return value.post.all()\

@register.filter(name='GetRemainingTime')
def get_class(posting_date):
    delta = datetime.now().date() - posting_date
    return str(delta.days) + " days"
