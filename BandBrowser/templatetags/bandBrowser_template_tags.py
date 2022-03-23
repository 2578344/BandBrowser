from django import template
from BandBrowser.models import UserProfile

register = template.Library()

def get_category_list():
    return {'users': UserProfile.objects.all()}

@register.inclusion_tag('BandBrowser/createPostPage.html')
def getBandList(user =None):
    userProfile = UserProfile.objects.get_or_create(user=user)[0]
    return {'userProfile': userProfile}
