from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from BandBrowser.models import Post
from BandBrowser.models import Band
from BandBrowser.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from datetime import datetime
from datetime import timedelta

def index(request):
    post_list = Post.objects.all()
    context_dict = {}
    context_dict["post"] = post_list
    return render(request, 'BandBrowser/index.html',context_dict)

def createBandPage(request):
    return render(request, 'BandBrowser/createBandPage.html')

def myBandPage(request):
    band_list = Band.objects.all()
    post_list = Post.objects.all()
    userProfile_list = UserProfile.objects.all()
    context_dict = {}
    context_dict["bands"] = band_list
    context_dict["post"] = post_list
    context_dict["userProfile"] = userProfile_list
    return render(request, 'BandBrowser/myBandPage.html',context_dict)

def createPostPage(request):
    context_dict = {}

    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)

    bands = userProfile.band.all()
    context_dict["bands"] = bands
    context_dict["userProfile"] = userProfile
    return render(request, 'BandBrowser/OtherCreatePostPage.html',context=context_dict)

def createUserPost(request):

    postID = datetime.now().strftime("%m%d%Y%H%M%S")
    title = request.POST.get('title')
    description = request.POST.get('description')
    location = request.POST.get('location')
    genre = request.POST.get('genre')
    commitment = request.POST.get('commitment')
    experience = request.POST.get('experience')
    expiresIn = request.POST.get('expiresIn')

    #VALIDATE POST

    post = Post.objects.get_or_create(postID=postID)[0]
    post.title = title
    publishDate = datetime.now()
    post.expireDate = publishDate + timedelta(days= int(expiresIn))
    post.experienceRequired = experience
    post.location = location
    post.genre = genre
    post.commitment = commitment
    post.description = description
    post.save()

    #pull user who wants to create the post - so we can add the post to them
    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)
    userProfile.post.add(post)
    userProfile.save()
    return render(request, 'BandBrowser/index.html')

def createBandPost(request):
    postID = datetime.now().strftime("%m%d%Y%H%M%S")
    title = request.POST.get('title')
    description = request.POST.get('description')
    location = request.POST.get('location')
    genre = request.POST.get('genre')
    commitment = request.POST.get('commitment')
    experience = request.POST.get('experience')
    expiresIn = request.POST.get('expiresIn')

    #VALIDATE POST

    post = Post.objects.get_or_create(postID=postID)[0]
    post.title = title
    publishDate = datetime.now()
    post.expireDate = publishDate + timedelta(days= int(expiresIn))
    post.experienceRequired = experience
    post.location = location
    post.genre = genre
    post.commitment = commitment
    post.description = description
    post.save()

    #pull user who wants to create the post - so we can add the post to them
    print(request.POST.get("band"))
    band = Band.objects.get(slug=request.POST.get("band"))
    band.post.add(post)
    band.save()
    return render(request, 'BandBrowser/index.html')

def loginPage(request):
    return render(request, 'BandBrowser/login.html')

@login_required
def accountPage(request):
    context_dict = {}

    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)

    context_dict["userProfile"] = userProfile
    return render(request, 'BandBrowser/AccountPage.html',context=context_dict)


def createAccountPage(request):
    return render(request, 'BandBrowser/CreateAccount.html')

def userLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                print("user logged in")
                return redirect(reverse('BandBrowser:index'))
            else:
                print("Your account is disabled")
                return HttpResponse("Your BandBrowser account is disabled.")
        else:

            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")


    else:
        return render(request, 'BandBrowser/login.html')

def logoutUser(request):
    logout(request)
    return redirect("BandBrowser:index")

def registerUser(request):
    registered = False
    if request.method == 'POST':
        #pull user attributes

        username = request.POST.get('username')
        password = request.POST.get('password')
        firstName = request.POST.get('First name')
        lastName = request.POST.get('Last name')
        dob = request.POST.get('DOB')
        email = request.POST.get('Email')

        #pull UserExternal libraries for linked accounts

        instruments = request.POST.get('Main-Instrument')+"&"+request.POST.get('second-Instrument')
        bio = request.POST.get('description')

        user = User.objects.create_user(username, email, password)
        user.first_name = firstName
        user.last_name = lastName
        user.save()

        userProfile = UserProfile.objects.get_or_create(user=user)[0]
        userProfile.instruments =instruments
        userProfile.dob = dob
        userProfile.linkedAccounts = ""
        userProfile.bio = bio
        userProfile.numberOfBands = 0
        userProfile.numberOfPostsActive = 0


        #VALIDATE USER i.e user.check_password("bar")
        userProfile.save()
        registered = True
        login(request,user)
        return render(request, 'BandBrowser/index.html')

def bandInfoPage(request):
    return render(request, 'BandBrowser/BandInfo.html')

def createBand(request):
    created = False
    if request.method == 'POST':
       #pull user who wants to create band - so we can add it to the correct account
       user = User.objects.get(username=request.user)
       userProfile = UserProfile.objects.get(user = user)

       name = request.POST.get('band-name')
       location = request.POST.get('location')
       genre = request.POST.get('genre')
       commitment = request.POST.get('levelOfCommitment')
       description = request.POST.get('description')

       #VALIDATE BAND

       band = Band.objects.get_or_create(name=name)[0]
       band.genres = genre
       band.commitment = commitment
       band.location = location
       band.description = description
       band.dateCreated = datetime.datetime.now()
       band.numberOfPostsActive = 0
       band.numberOfCurrentMembers = 0
       band.numberOfPotentialMembers = 0
       band.currentMember.add(userProfile.user)
       band.save()


       return render(request, 'BandBrowser/BandInfo.html')