from django import forms
from django.contrib.auth.models import User
from BandBrowser.models import Post
from BandBrowser.models import Band
from BandBrowser.models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('avatar',)