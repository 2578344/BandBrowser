import os
import datetime
from datetime import timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project7.settings')

import django
django.setup()
from BandBrowser.models import UserProfile, Band, Post
from django.contrib.auth.models import User

userInstances =[]
bandInstances =[]
postInstances =[]
def populate():

    usersRaw = [
        {"username":"Alex","instruments":"Banjo","Bio":"Hi","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"John","instruments":"Bass","Bio":"Hello","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Tom","instruments":"Drums","Bio":"Howdy","numberOfBands":0,"numberOfPostsActive":0}
    ]

    bandsRaw = [
        {"name":"Joy Division","genres":"Post Punk","commitment":"Full Time","location":"Manchester","dateCreated":datetime.date(1976, 10, 19)},
        {"name":"The Joy Formidable","genres":"Alternative","commitment":"When We can","location":"Wales","dateCreated":datetime.date(2007, 12, 8)},
        {"name":"Interpol","genres":"Post Punk","commitment":"Weekly","location":"New York","dateCreated":datetime.date(1997, 5, 28)}
    ]

    postsRaw = [
        {"postID":"0","description":"ASAP","title":"Bassist Wanted","publishDate":datetime.date(2022, 3, 9),"expireDate":datetime.date(2022, 3, 9)+ timedelta(days=10),"experienceRequired":"Some","genres":"Post Punk","commitment":"Full Time","location":"Manchester"},
        {"postID":"1","description":"Just Started the band","title":"Drummer Needed","publishDate":datetime.date(2022, 3, 16),"expireDate":datetime.date(2022, 3, 16)+ timedelta(days=10),"experienceRequired":"None","genres":"Alternative","commitment":"When We can","location":"Wales"},
        {"postID":"2","description":"Guitarist seeks band","title":"Looking For Band","publishDate":datetime.date(2022, 3, 22),"expireDate":datetime.date(2022, 3, 22)+ timedelta(days=10),"experienceRequired":"A lot","genres":"Jazz","commitment":"Full Time","location":"Glasgow"}
    ]

    #create User and UserProfile objects, link them together
    for user_data in usersRaw:
        if not User.objects.filter(username=user_data["username"]).exists():
            user = add_User(user_data["username"])
            user.save()
            print(add_UserProfile(user,user_data["instruments"],user_data["Bio"],user_data["numberOfBands"],user_data["numberOfPostsActive"]).bio)
    for users in userInstances:
        print(users.user.username)

    #create Band objects
    for band_data in bandsRaw:
        if not Band.objects.filter(name=band_data["name"]).exists():
            print(add_band(band_data["name"],band_data["genres"],band_data["commitment"],band_data["location"],band_data["dateCreated"]).name)
    for bands in bandInstances:
        print(bands.genres)

    #create Post objects
    for post_data in postsRaw:
        if not Post.objects.filter(postID=post_data["postID"]).exists():
            print(add_post(post_data["postID"],post_data["description"],post_data["title"],post_data["publishDate"],post_data["expireDate"],post_data["experienceRequired"],post_data["genres"],post_data["commitment"],post_data["location"]).title)
    for post in postInstances:
        print(post.expireDate)


#user functions
def add_User(username,email=None, password=None):
    user = User.objects.create_user(username, email, password)
    return user

def add_UserProfile(user,instruments,bio,numberOfBands=0,numberOfPostsActive=0):
    user = UserProfile.objects.get_or_create(user=user)[0]
    user.instruments =instruments
    user.linkedAccounts =""
    user.bio = bio
    user.numberOfBands =numberOfBands
    user.numberOfPostsActive =numberOfPostsActive
    user.save()
    userInstances.append(user)
    return user

#band functions
def add_band(name,genres,commitment,location,dateCreated):
    band = Band.objects.get_or_create(name=name)[0]
    band.genres = genres
    band.commitment = commitment
    band.location = location
    band.dateCreated = dateCreated
    band.numberOfPostsActive = 0
    band.numberOfCurrentMembers = 0
    band.numberOfPotentialMembers = 0
    band.save()
    bandInstances.append(band)
    return band

#post functions
def add_post(postID,description,title,publishDate,expireDate,experienceRequired,genre,commitment,location):
    post = Post.objects.get_or_create(postID=postID)[0]
    post.title = title
    post.publishDate = publishDate
    post.expireDate = expireDate
    post.experienceRequired = experienceRequired
    post.location = location
    post.genre = genre
    post.commitment = commitment
    post.description = description
    post.save()
    postInstances.append(post)
    return post

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
