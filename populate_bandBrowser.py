import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project7.settings')

import django
django.setup()
from BandBrowser.models import UserProfile, Band, Post

def populate():


def add_UserProfile(user, title, url, views=0, likes = 0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.likes=likes
    p.save()
    return p

def add_cat(name,views = 0,likes = 0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
