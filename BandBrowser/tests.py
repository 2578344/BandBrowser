from django.test import TestCase
from BandBrowser.models import Post, Band, UserProfile
from datetime import datetime
from django.contrib.auth.models import User



class BandMethodTest(TestCase):
    
    name = "Band1"
    genres = "Rock"
    commitment = "none"
    location = "Glasgow"
    description = "looking for members"
    dateCreated = datetime.now()
    numberOfPostsActive = 2
    numberOfCurrentMembers = 3
    numberOfPotentialMembers = 1

    ###test post
    postID = "933"
    description = "description"
    title = "first"
    publishDate = datetime.now()
    expireDate = datetime.now()
    experienceRequired = "junior"
    location = "Glasgow"
    genre = "Rock"
    commitment = "drums"
    

    def test_check_if_band_created(self):
        post1 = make_test_post(
                            postID=self.postID,
                            description=self.description,
                            title=self.title,
                            publishDate=self.publishDate,
                            expireDate=self.expireDate,
                            experienceRequired=self.experienceRequired,
                            location=self.location,
                            genre=self.genre,
                            commitment=self.commitment)        
        currentMember = make_test_user("member1","pass")
        potentialMember = make_test_user("potential member","123")

        band = make_test_band(
            post=post1.set(),
            name=self.name,
            genres=self.genres,
            commitment=self.commitment,
            location=self.location,
            description=self.description,
            dateCreated=self.dateCreated,
            numberOfPostsActive=self.numberOfPostsActive,
            numberOfCurrentMembers=self.numberOfCurrentMembers,
            numberOfPotentialMembers=self.numberOfPotentialMembers,
            currentMember=currentMember,
            potentialMember=potentialMember)
        band.save()

        self.assertEquals((band.name==self.name), True)

class PostMethodTest(TestCase):
    postID = "933"
    description = "description"
    title = "first"
    publishDate = datetime.now()
    expireDate = datetime.now()
    experienceRequired = "junior"
    location = "Glasgow"
    genre = "Rock"
    commitment = "drums"

    def test_check_if_created(self):
        post = make_test_post(
                            postID=self.postID,
                            description=self.description,
                            title=self.title,
                            publishDate=self.publishDate,
                            expireDate=self.expireDate,
                            experienceRequired=self.experienceRequired,
                            location=self.location,
                            genre=self.genre,
                            commitment=self.commitment)
        post.save()
        self.assertEquals((post.description==self.description), True)
        self.assertEquals((post.postID==self.postID), True)
        self.assertEquals((post.title==self.title), True)
        self.assertEquals((post.publishDate==self.publishDate), True)
        self.assertEquals((post.expireDate==self.expireDate), True)
        self.assertEquals((post.experienceRequired==self.experienceRequired), True)
        self.assertEquals((post.location==self.location), True)
        self.assertEquals((post.genre==self.genre), True)
        self.assertEquals((post.commitment==self.commitment), True)


# class UserProfileTest(TestCase):
    
    
#     dob =  datetime.date.today())
#     band = models.ManyToManyField(Band)
#     post = models.ManyToManyField(Post)
#     instruments = "guitar"
#     linkedAccounts = "nothing"
#     bio = "team player"
#     numberOfBands = 3
#     numberOfPostsActive = 2

#     # test post
#     postID = "933"
#     description = "description"
#     title = "first"
#     publishDate = datetime.now()
#     expireDate = datetime.now()
#     experienceRequired = "junior"
#     location = "Glasgow"
#     genre = "Rock"
#     commitment = "drums"

#     def test_check_if_userprofile_created(self):
#         user = make_test_user("Daniel","example")
#         post1 = make_test_post(
#                             postID=self.postID,
#                             description=self.description,
#                             title=self.title,
#                             publishDate=self.publishDate,
#                             expireDate=self.expireDate,
#                             experienceRequired=self.experienceRequired,
#                             location=self.location,
#                             genre=self.genre,
#                             commitment=self.commitment)

class UserMethodTest(TestCase):
    username="Alex"
    password="Example123?"


    def test_check_if_created_user(self):
        user = make_test_user(self.username,self.password)
        user.save()
        self.assertEquals((user.username==self.username), True)

###############
def make_test_post(postID,description,title,publishDate,expireDate,experienceRequired,genre,commitment,location):
    p = Post(
            postID=postID,
            description=description,
            title=title,
            publishDate=publishDate,
            expireDate=expireDate,
            experienceRequired=experienceRequired,
            genre=genre,
            commitment=commitment,
            location=location)
    return p

def make_test_user(username,password):
    u = User(username=username,
            password=password)
    return u



def make_test_band(post,name,genres,commitment,
                location,description,dateCreated,
                numberOfPostsActive,
                numberOfCurrentMembers,
                numberOfPotentialMembers,
                currentMember,
                potentialMember):
    b = Band(post=post,
            name=name,
            genres=genres,
            commitment=commitment,
            location=location,
            description=description,
            dateCreated=dateCreated,
            numberOfPostsActive=numberOfPostsActive,
            numberOfCurrentMembers=numberOfCurrentMembers,
            numberOfPotentialMembers=numberOfPotentialMembers,
            currentMember=currentMember,
            potentialMember=potentialMember)
    return b