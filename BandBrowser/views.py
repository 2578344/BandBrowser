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
    context_dict = {}
    context_dict["bands"] = band_list
    context_dict["post"] = post_list
    return render(request, 'BandBrowser/myBandPage.html',context_dict)

def createPostPage(request):
    return render(request, 'BandBrowser/createPostPage.html')

def loginPage(request):
    return render(request, 'BandBrowser/login.html')

@login_required
def accountPage(request):
    return render(request, 'BandBrowser/AccountPage.html')

def index(request):
    return render(request, 'BandBrowser/index.html')

def index(request):
    return render(request, 'BandBrowser/index.html')

def index(request):
    return render(request, 'BandBrowser/index.html')

def index(request):
    return render(request, 'BandBrowser/index.html')

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
        user.save()

        userProfile = UserProfile.objects.get_or_create(user=user)[0]
        userProfile.instruments =instruments
        userProfile.linkedAccounts = ""
        userProfile.bio = bio
        userProfile.numberOfBands = 0
        userProfile.numberOfPostsActive = 0

        #VALIDATE USER i.e user.check_password("bar")
        userProfile.save()
        registered = True
        login(request,user)
        return render(request, 'BandBrowser/index.html')