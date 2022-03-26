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
from django.template.defaultfilters import slugify
from BandBrowser.forms import UserProfileForm

def index(request):
    entitiesWhoHavePosts = []
    for band in Band.objects.all():
        if band.post.exists():
            print(band)
            entitiesWhoHavePosts.append(band)
    for user in UserProfile.objects.all():
        if user.post.exists():
            print(user)
            entitiesWhoHavePosts.append(user)

    post_list = Post.objects.all()
    context_dict = {}
    print(request.user)
    if(request.user.is_anonymous ==False):
        user = User.objects.get(username=request.user)
        userProfile = UserProfile.objects.get(user = user)
        context_dict["userProfileBands"] = userProfile.band.all()
        context_dict["userProfile"] = userProfile
    context_dict["ModelsHavePosts"] = entitiesWhoHavePosts
    context_dict["post"] = post_list
    return render(request, 'BandBrowser/index.html',context_dict)

# =============================================== POST Functions ===============================================

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
    userProfile.numberOfPostsActive = userProfile.numberOfPostsActive +1
    userProfile.save()
    return redirect("BandBrowser:index")

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
    band.numberOfPostsActive = band.numberOfPostsActive + 1
    band.save()
    return redirect("BandBrowser:index")

def AddPostUserToBand(request):

    band = Band.objects.get(slug=request.POST.get("band"))

    userToAddToBand = User.objects.get(username=request.POST.get("userToAdd"))
    userProfileToAddToBand = UserProfile.objects.get(user = userToAddToBand)

    band.currentMember.add(userToAddToBand)
    band.numberOfCurrentMembers = band.numberOfCurrentMembers +1
    band.save()

    userProfileToAddToBand.band.add(band)
    userProfileToAddToBand.numberOfBands = userProfileToAddToBand.numberOfBands +1
    userProfileToAddToBand.save()

    return redirect("BandBrowser:index")

def AddUserToRequestMembers(request):

    band = Band.objects.get(slug=request.POST.get("bandToRequestJoin"))

    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)

    band.potentialMember.add(user)
    band.numberOfPotentialMembers = band.numberOfPotentialMembers +1
    band.save()

    return redirect("BandBrowser:index")
# =============================================== User Functions ===============================================

def loginPage(request):
    return render(request, 'BandBrowser/login.html')

@login_required
def accountPage(request):
    context_dict = {}

    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)

    context_dict["userProfile"] = userProfile
    context_dict["form"] = UserProfileForm()

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
                return redirect("BandBrowser:index")
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

        instruments = request.POST.get('Main-Instrument')
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
        return redirect("BandBrowser:index")

def uploadUserAvatar(request):
    print("request")
    form = UserProfileForm(request.POST, request.FILES)
    if form.is_valid():
        data= form.cleaned_data.get("avatar")
        print(data)
        # Get the current instance object to display in the template
        img_obj = form.instance
        HttpResponse('successfully uploaded')


def updateUserAccount(request):
    registered = False
    if request.method == 'POST':
        #pull user attributes
        firstName = request.POST.get('First name')
        lastName = request.POST.get('Last name')
        dob = request.POST.get('DOB')
        email = request.POST.get('Email')

        #img = Image.open(self.image.path) # Open image
        #pull UserExternal libraries for linked accounts

        instruments = request.POST.get('Main-Instrument')
        bio = request.POST.get('Bio')

        user = User.objects.get(username=request.user)
        user.first_name = firstName
        user.last_name = lastName
        user.email = email
        user.save()

        userProfile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            tempUserProfileform = form.save(commit=False)
            file= form.cleaned_data.get("avatar")
            if file is not None:
                userProfile.avatar = tempUserProfileform.avatar
        userProfile.instruments =instruments
        userProfile.dob = dob
        userProfile.linkedAccounts = "&&"
        userProfile.bio = bio


        #VALIDATE USER i.e user.check_password("bar")
        userProfile.save()
        return redirect("BandBrowser:accountPage")

def deleteUserAccount(request):
    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)

    #need to delete any bands the user may be in (if they are the only user)
    for band in Band.objects.filter(currentMember = user):
        if band.currentMember.count() == 1:
            #need to delete any posts the band may have made
            for post in band.post.all():
                post.delete()
            band.delete()
    for post in userProfile.post.all():
        post.delete()
    #need to delete any posts the user may have
    user.delete()
    userProfile.delete()
    return redirect("BandBrowser:index")

def viewUserPage(request):
    context_dict = {}
    print(request.POST.get("userToView"))
    userToView = User.objects.get(username=request.POST.get("userToView"))
    userToViewProfile = UserProfile.objects.get(user = userToView)

    context_dict["userToViewProfile"] = userToViewProfile
    return render(request, 'BandBrowser/ViewUserPage.html',context=context_dict)

def viewBandPage(request):
    context_dict = {}
    print("A"+request.POST.get("BandToView"))
    bandToView = Band.objects.get(slug=request.POST.get("BandToView"))
    context_dict["BandToView"] = bandToView
    context_dict["CurrentMembers"] = bandToView.currentMember.all()
    context_dict["potentialMember"] = bandToView.potentialMember.all()


    return render(request, 'BandBrowser/ViewBandPage.html',context=context_dict)

# =============================================== Band Functions ===============================================

def createBandPage(request):
    return render(request, 'BandBrowser/createBandPage.html')

def myBandPage(request):
    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)

    bands = userProfile.band.all()
    context_dict = {}
    context_dict["bands"] = bands
    context_dict["userProfile"] = userProfile
    return render(request, 'BandBrowser/myBandPage.html',context_dict)

def bandInfoPage(request):

    context_dict = {}
    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)
    band = Band.objects.get(slug=request.POST.get("bandName"))
    context_dict["band"] = band
    context_dict["CurrentMembers"] = band.currentMember.all()
    context_dict["potentialMember"] = band.potentialMember.all()
    context_dict["userProfile"] = userProfile
    return render(request, 'BandBrowser/BandInfo.html',context_dict)

def updateBandInfo(request):
    if request.method == 'POST':
        #pull user attributes
        band = Band.objects.get(name = request.POST.get('oldBandName'))
        name = request.POST.get('Bandname')
        location = request.POST.get('Location')
        genre = request.POST.get('genres')
        commitment = request.POST.get('commitment')
        description = request.POST.get('description')

        #VALIDATE BAND

        band.name = name
        band.genres = genre
        band.commitment = commitment
        band.location = location
        band.description = description
        band.save()

        context_dict = {}
        user = User.objects.get(username=request.user)
        userProfile = UserProfile.objects.get(user = user)
        context_dict["band"] = band
        context_dict["CurrentMembers"] = band.currentMember.all()
        context_dict["potentialMember"] = band.potentialMember.all()
        context_dict["userProfile"] = userProfile

        return render(request, 'BandBrowser/BandInfo.html',context_dict)

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
        band.dateCreated = datetime.now()
        band.numberOfPostsActive = 0
        band.numberOfCurrentMembers = 0
        band.numberOfPotentialMembers = 0
        band.currentMember.add(userProfile.user)
        band.save()
        userProfile.band.add(band)
        userProfile.save()

        context_dict = {}
        user = User.objects.get(username=request.user)
        userProfile = UserProfile.objects.get(user = user)
        context_dict["band"] = band
        context_dict["CurrentMembers"] = band.currentMember.all()
        context_dict["potentialMember"] = band.potentialMember.all()
        context_dict["userProfile"] = userProfile

        return render(request, 'BandBrowser/BandInfo.html',context_dict)

def removeCurrentBandMember(request):
    band = Band.objects.get(slug = request.POST.get('bandName'))
    userToRemove = User.objects.get(username= request.POST.get('memberToRemove'))
    userProfileToRemove = UserProfile.objects.get(user = userToRemove)

    #remove the band from the user
    userProfileToRemove.band.remove(band)
    #remove the user from the band
    band.currentMember.remove(userProfileToRemove.user)
    userProfileToRemove.numberOfBands = userProfileToRemove.numberOfBands -1
    userProfileToRemove.band.remove(band)
    band.numberOfCurrentMembers = band.numberOfCurrentMembers -1
    band.save()
    userProfileToRemove.save()

    context_dict = {}
    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)
    context_dict["band"] = band
    context_dict["CurrentMembers"] = band.currentMember.all()
    context_dict["potentialMember"] = band.potentialMember.all()
    context_dict["userProfile"] = userProfile

    return render(request, 'BandBrowser/BandInfo.html',context_dict)

def acceptUserJoinRequest(request):
    band = Band.objects.get(slug = request.POST.get('bandName'))

    userToJoin = User.objects.get(username=request.POST.get('userToJoin'))
    userProfileToJoin = UserProfile.objects.get(user = userToJoin)

    #add user to the band
    band.currentMember.add(userToJoin)
    band.numberOfCurrentMembers = band.numberOfCurrentMembers+1
    band.numberOfPotentialMembers = band.numberOfPotentialMembers-1
    band.potentialMember.remove(userToJoin)
    band.save()

    #add band to user
    userProfileToJoin.band.add(band)
    userProfileToJoin.numberOfBands = userProfileToJoin.numberOfBands +1
    userProfileToJoin.save()

    context_dict = {}
    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)
    print(userProfile.user.username)
    context_dict["band"] = band
    context_dict["CurrentMembers"] = band.currentMember.all()
    context_dict["potentialMember"] = band.potentialMember.all()
    context_dict["userProfile"] = userProfile

    return render(request, 'BandBrowser/BandInfo.html',context_dict)

def declineUserJoinRequest(request):
    band = Band.objects.get(slug = request.POST.get('bandName'))
    userNotToJoin = User.objects.get(username=request.POST.get('userNotToJoin'))

    #add user to the band
    band.numberOfPotentialMembers = band.numberOfPotentialMembers-1
    band.potentialMember.remove(userNotToJoin)
    band.save()

    context_dict = {}
    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)
    context_dict["band"] = band
    context_dict["CurrentMembers"] = band.currentMember.all()
    context_dict["potentialMember"] = band.potentialMember.all()
    context_dict["userProfile"] = userProfile

    return render(request, 'BandBrowser/BandInfo.html',context_dict)

def leaveBand(request):
    band = Band.objects.get(slug = request.POST.get('bandSlug'))
    user = User.objects.get(username=request.user)
    userProfile = UserProfile.objects.get(user = user)
    print(userProfile.user.username)
    userProfile.band.remove(band)
    userProfile.numberOfBands = userProfile.numberOfBands -1
    userProfile.save()
    band.currentMember.remove(user)
    band.save()
    #if the only member is themselves the band will be deleted
    if(band.currentMember.count() ==0):
        for post in band.post.all():
            post.delete()
        band.delete()
    bands = userProfile.band.all()
    context_dict = {}
    context_dict["bands"] = bands
    context_dict["userProfile"] = userProfile
    return render(request, 'BandBrowser/myBandPage.html',context_dict)