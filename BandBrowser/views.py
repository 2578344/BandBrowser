from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from BandBrowser.models import Post
from BandBrowser.models import Band
from django.contrib.auth.decorators import login_required

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