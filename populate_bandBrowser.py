import os
import datetime
from datetime import timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project7.settings')

import django
django.setup()
from BandBrowser.models import UserProfile, Band, Post
from django.contrib.auth.models import User

userProfileInstances =[]#UserProflie instances not User
bandInstances =[]
postInstances =[]
def populate():

    print("===================")

    deleteInstances()#clear any current instances (that are not admin) and replace with the data set

    print("===================")

    usersRaw = [
        #Interpol Members
        {"username":"Paul","first_name":"Paul","last_name":"Banks","password":"Example123?","instruments":"Vocals","Bio":"Hi","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Daniel","first_name":"Daniel","last_name":"Kessler","password":"Example123?","instruments":"Guitar","Bio":"Hello","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Sam","first_name":"Sam","last_name":"Fogarino","password":"Example123?","instruments":"Drums","Bio":"Howdy","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Carlos","first_name":"Sam","last_name":"Dengler","password":"Example123?","instruments":"Bass","Bio":"Howdy","numberOfBands":0,"numberOfPostsActive":0},
        #Joy Division and New Order Members
        {"username":"Ian","first_name":"Ian","last_name":"Curtis","password":"Example123?","instruments":"Vocals","Bio":"Hello there","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Peter","first_name":"Peter","last_name":"Hook","password":"Example123?","instruments":"Bass","Bio":"Hi ya","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Stephen","first_name":"Stephen","last_name":"Morris","password":"Example123?","instruments":"Drums","Bio":"Hi","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Bernard","first_name":"Bernard","last_name":"Sumner","password":"Example123?","instruments":"Guitar","Bio":"Hello","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Gillian","first_name":"Gillian","last_name":"Gilbert","password":"Example123?","instruments":"Guitar","Bio":"Howdy","numberOfBands":0,"numberOfPostsActive":0},
        #The Joy Formidable Members
        {"username":"Ritzy","first_name":"Rhiannon ","last_name":"Bryan","password":"Example123?","instruments":"Vocals","Bio":"Hi ya","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Rhydian","first_name":"Rhydian","last_name":"Dafydd","password":"Example123?","instruments":"Bass","Bio":"Hello","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Matthew","first_name":"Matthew","last_name":"Thomas","password":"Example123?","instruments":"Drums","Bio":"Hey","numberOfBands":0,"numberOfPostsActive":0},
        #Bronski Beat Members
        {"username":"Jimmy ","first_name":"Jimmy","last_name":"Somerville","password":"Example123?","instruments":"Vocals","Bio":"Hello There","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Steve","first_name":"Steve","last_name":"Bronski","password":"Example123?","instruments":"Drums","Bio":"Hello","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"Larry","first_name":"Larry","last_name":"Steinbachek","password":"Example123?","instruments":"Bass","Bio":"Hi","numberOfBands":0,"numberOfPostsActive":0},
        #Beastie Boys
        {"username":"MikeD ","first_name":"Michael","last_name":"Diamond","password":"Example123?","instruments":"Drums","Bio":"Hey","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"MCA","first_name":"Adam","last_name":"Yauch","password":"Example123?","instruments":"Bass","Bio":"Hello","numberOfBands":0,"numberOfPostsActive":0},
        {"username":"ADRock","first_name":"Adam","last_name":"Horovitz","password":"Example123?","instruments":"Guitar","Bio":"Hi","numberOfBands":0,"numberOfPostsActive":0}


    ]

    bandsRaw = [
        {"name":"Interpol","genres":"Rock","commitment":"Weekly","location":"New York","dateCreated":datetime.date(1997, 5, 28)},
        {"name":"Joy Division","genres":"Rock","commitment":"Full Time","location":"Manchester","dateCreated":datetime.date(1976, 10, 19)},
        {"name":"New Order","genres":"Pop","commitment":"Full Time","location":"Manchester","dateCreated":datetime.date(1980 , 5, 20)},
        {"name":"The Joy Formidable","genres":"Rap","commitment":"Whenever","location":"Wales","dateCreated":datetime.date(2007, 12, 8)},
        {"name":"Bronski Beat","genres":"Pop","commitment":"Daily","location":"Glasgow","dateCreated":datetime.date(1985, 1, 12)},
        {"name":"Beastie Boys","genres":"Rap","commitment":"Whenever","location":"New York","dateCreated":datetime.date(1978, 10, 28)}
    ]

    postsRaw = [
        {"postID":"0","description":"ASAP","title":"Looking For a bassist","publishDate":datetime.date(2022, 3, 9),"expireDate":datetime.date(2022, 3, 9)+ timedelta(days=10),"experienceRequired":"Some","genres":"Rock","commitment":"Full Time","location":"Manchester","Type":"Band"},
        {"postID":"1","description":"Just Started the band","title":"Looking For a drummer","publishDate":datetime.date(2022, 3, 16),"expireDate":datetime.date(2022, 3, 16)+ timedelta(days=10),"experienceRequired":"None","genres":"Alternative","commitment":"When We can","location":"Wales","Type":"Band"},
        {"postID":"2","description":"Guitarist seeks band","title":"Looking For Band as a guitarist","publishDate":datetime.date(2022, 3, 22),"expireDate":datetime.date(2022, 3, 22)+ timedelta(days=10),"experienceRequired":"A lot","genres":"Jazz","commitment":"Full Time","location":"Glasgow","Type":"User"},
        {"postID":"3","description":"Rap Group looking for touring bassist","title":"Looking For Bassist","publishDate":datetime.date(2022, 3, 24),"expireDate":datetime.date(2022, 3, 22)+ timedelta(days=10),"experienceRequired":"A lot","genres":"Rap","commitment":"Full Time","location":"Manchester","Type":"Band"},
        {"postID":"4","description":"Vocalist seeks band","title":"Looking For Band as a vocalist","publishDate":datetime.date(2022, 3, 26),"expireDate":datetime.date(2022, 3, 22)+ timedelta(days=10),"experienceRequired":"A lot","genres":"Rock","commitment":"Full Time","location":"New Yok","Type":"User"}
    ]

    #create User and UserProfile objects, link them together
    for user_data in usersRaw:
        if not User.objects.filter(username=user_data["username"]).exists():
            user = add_User(user_data["username"],user_data["password"])
            user.first_name = user_data["first_name"]
            user.last_name = user_data["last_name"]
            user.save()
            add_UserProfile(user,user_data["instruments"],user_data["Bio"],user_data["numberOfBands"],user_data["numberOfPostsActive"])

    print("===================")

    #create Band objects
    for band_data in bandsRaw:
        if not Band.objects.filter(name=band_data["name"]).exists():
            add_band(band_data["name"],band_data["genres"],band_data["commitment"],band_data["location"],band_data["dateCreated"])

    print("===================")

    #create Post objects
    for post_data in postsRaw:
        if not Post.objects.filter(postID=post_data["postID"]).exists():
            add_post(post_data["postID"],post_data["description"],post_data["title"],post_data["publishDate"],post_data["expireDate"],post_data["experienceRequired"],post_data["genres"],post_data["commitment"],post_data["location"])

    print("===================")

    #attach a user to a band, goes in both directions
    #Interpol Members
    attachBandToUser(bandInstances[0],userProfileInstances[0])# Paul joins Interpol
    attachBandToUser(bandInstances[0],userProfileInstances[1])# Daniel joins Interpol
    attachBandToUser(bandInstances[0],userProfileInstances[2])# Sam joins Interpol
    attachBandToUser(bandInstances[0],userProfileInstances[3])# Carlos joins Interpol
    #Joy Division Members
    attachBandToUser(bandInstances[1],userProfileInstances[4])# Ian joins Joy Division
    attachBandToUser(bandInstances[1],userProfileInstances[5])# Peter joins Joy Division
    attachBandToUser(bandInstances[1],userProfileInstances[6])# Stephen joins Joy Division
    attachBandToUser(bandInstances[1],userProfileInstances[7])# Bernard joins Joy Division
    # New Order Members
    attachBandToUser(bandInstances[2],userProfileInstances[5])# Peter joins New Order
    attachBandToUser(bandInstances[2],userProfileInstances[6])# Stephen joins New Order
    attachBandToUser(bandInstances[2],userProfileInstances[7])# Bernard joins New Order
    attachBandToUser(bandInstances[2],userProfileInstances[8])# Gillian joins New Order
    #The Joy Formidable Members
    attachBandToUser(bandInstances[3],userProfileInstances[9])# Ritzy joins The Joy Formidable
    attachBandToUser(bandInstances[3],userProfileInstances[10])# Rhydian joins The Joy Formidable
    attachBandToUser(bandInstances[3],userProfileInstances[11])# Matthew joins The Joy Formidable
    #Bronski Beat Members
    attachBandToUser(bandInstances[4],userProfileInstances[12])# Jimmy joins Bronski Beat
    attachBandToUser(bandInstances[4],userProfileInstances[13])# Steve joins Bronski Beat
    attachBandToUser(bandInstances[4],userProfileInstances[14])# Larry joins Bronski Beat

    #Beastie Boys
    attachBandToUser(bandInstances[5],userProfileInstances[15])# MikeD joins Beastie Boys
    attachBandToUser(bandInstances[5],userProfileInstances[16])# MCA joins Beastie Boys
    attachBandToUser(bandInstances[5],userProfileInstances[17])# ADRock joins Beastie Boys

    print("===================")

    #attach posts (manually to user and band models)
    attachPostToUser(postInstances[2], userProfileInstances[17])#ADRock, guitarist seeks band
    attachPostToBand(postInstances[1], bandInstances[1])#The Joy Formidable looking for a drummer
    attachPostToBand(postInstances[0], bandInstances[0])#Interpol looking for a bassist
    attachPostToBand(postInstances[3], bandInstances[3])#Joy Division looking for a bassist
    attachPostToUser(postInstances[4], userProfileInstances[12])#Jimmy, vocalist seeks band

    print("===================")
    attachUserToBandAsPotentialMember(userProfileInstances[4],bandInstances[0])# peter requests to join joy division

#user functions
def add_User(username,password=None, email=None):
    user = User.objects.create_user(username, email, password)
    return user

def add_UserProfile(user,instruments,bio,numberOfBands=0,numberOfPostsActive=0):
    userProfile = UserProfile.objects.get_or_create(user=user)[0]
    userProfile.instruments =instruments
    userProfile.linkedAccounts =""
    userProfile.bio = bio
    userProfile.numberOfBands =numberOfBands
    userProfile.numberOfPostsActive =numberOfPostsActive
    userProfile.save()
    print(userProfile.user.username +" Account has been created")
    userProfileInstances.append(userProfile)
    return userProfile

def attachPostToUser(post, userProfile):
    posts = userProfile.post
    if not posts.exists():
        userProfile.post.add(post)
        userProfile.numberOfPostsActive = userProfile.numberOfPostsActive +1
        userProfile.save()
        print(userProfile.user.username+" is "+ post.title+ "!")

def attachBandToUser(bandToJoin, userProfile):
    #first we add the band to the user
    band = userProfile.band.filter(name=bandToJoin.name)
    if not band.exists():
        userProfile.band.add(bandToJoin)
        userProfile.numberOfBands = userProfile.numberOfBands +1
        userProfile.save()
        #now we need to add the user to the band
        attachUserToBandAsCurrentMember(userProfile,bandToJoin)



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
    band.description =""
    band.save()
    print(band.name +" Band has been created")
    bandInstances.append(band)
    return band

def attachPostToBand(post, band):
    posts = band.post
    if not posts.exists():
        band.post.add(post)
        band.numberOfPostsActive = band.numberOfPostsActive +1
        band.save()
        print(band.name+" "+ post.title+ "!")

def attachUserToBandAsCurrentMember(userProfileToJoin,band):
    user = band.currentMember.filter(username= userProfileToJoin.user.username)
    if not user.exists():
        band.currentMember.add(userProfileToJoin.user)
        band.numberOfCurrentMembers = band.numberOfCurrentMembers +1
        band.save()
        print(userProfileToJoin.user.username+" has joined "+ band.name+ "!")

def attachUserToBandAsPotentialMember(userProfileToRequest,band):
    user = band.potentialMember.filter(username= userProfileToRequest.user.username)
    if not user.exists():
        band.potentialMember.add(userProfileToRequest.user)
        band.numberOfPotentialMembers = band.numberOfPotentialMembers +1
        band.save()
        print(userProfileToRequest.user.username+" has requested to join "+ band.name+ "!")



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
    print(post.title +" Post has been created")
    postInstances.append(post)
    return post



#all objects functions
def getInstances():
    for band in Band.objects.all():
        if not band in bandInstances:
            bandInstances.append(bandInstances)
        print(band.name+" added")
    for user in UserProfile.objects.all():
        if not user.user in userProfileInstances:
            userProfileInstances.append(user.user)
        print(user.user.username+" added")
    for post in Post.objects.all():
        if not post in postInstances:
            postInstances.append(post)
        print(post.title+" added")

def deleteInstances():
    print("Previous records have been deleted")
    for band in Band.objects.all():
        band.delete()
    for user in User.objects.filter(is_staff=False):
        user.delete()
    for post in Post.objects.all():
        post.delete()

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()