from django.db import models
from django.template.defaultfilters import slugify
from tabnanny import verbose
from django.contrib.auth.models import User
import datetime
from datetime import timedelta
from django.core.exceptions import ValidationError

class Post(models.Model):
    TITLE_MAX_LENGTH=128
    postID = models.CharField(max_length=11, unique=True)
    description = models.CharField(max_length=1000)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    publishDate = models.DateField(max_length=128,default = datetime.date.today())
    expireDate = models.DateField(default = datetime.date.today()+ timedelta(days=10))
    experienceRequired = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    genre = models.CharField(max_length=32)
    commitment = models.CharField(max_length=32)

    def clean(self):
        if len(self.description) > 1000:
            raise ValidationError(
                {'description': "Description should be less than 1000 characters"})
        if  len(self.title) < 10:
            raise ValidationError(
                {'title': "Title should have at least 10 characters"})
        if  len(self.experienceRequired) == 0:
            raise ValidationError(
                {'experienceRequired': "Please select a type of experience required"})

        if  len(self.location) == 0:
            raise ValidationError(
                {'location': "Please enter a location you want to play in"})

        if  len(self.genre) == 0:
            raise ValidationError(
                {'genre': "Please enter a genre"})

        if  len(self.commitment) == 0:
            raise ValidationError(
                {'commitment': "Please select how committed you are"})

    def __str__(self):
        return self.title


class Band(models.Model):
    NAME_MAX_LENGTH = 128
    post = models.ManyToManyField(Post)
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    genres = models.CharField(max_length=32)
    commitment = models.CharField(max_length=32)
    location = models.CharField(max_length=128)
    description = models.TextField(default ="")
    dateCreated = models.DateField(max_length=128, default = datetime.date.today())
    numberOfPostsActive = models.IntegerField(default=0)
    numberOfCurrentMembers = models.IntegerField(default=0)
    numberOfPotentialMembers = models.IntegerField(default=0)
    currentMember = models.ManyToManyField(User,related_name='Current_Members')
    potentialMember = models.ManyToManyField(User,related_name='Potential_Members')
    slug = models.SlugField(unique=True)

    def clean(self):
        if len(self.description) > 1000:
            raise ValidationError(
                {'description': "Description should be less than 1000 characters"})
        if  len(self.name) < 10:
            raise ValidationError(
                {'name': "Title should have at least 10 characters"})
        if  len(self.experienceRequired) == 0:
            raise ValidationError(
                {'experienceRequired': "Please select a type of experience required"})

        if  len(self.location) == 0:
            raise ValidationError(
                {'location': "Please enter a location you want to play in"})

        if  len(self.genres) == 0:
            raise ValidationError(
                {'genres': "Please enter a genre"})

        if  len(self.commitment) == 0:
            raise ValidationError(
                {'commitment': "Please select how committed you are"})


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Band, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Bands'

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(max_length=128, default = datetime.date.today())
    band = models.ManyToManyField(Band)
    post = models.ManyToManyField(Post)
    instruments = models.TextField()
    linkedAccounts = models.TextField()
    bio = models.TextField()
    avatar = models.ImageField(upload_to='profile_images', blank=True)
    numberOfBands = models.IntegerField(default=0)
    numberOfPostsActive = models.IntegerField(default=0)

    def cleanit(self):
        if len(self.user.first_name) == 0:
            raise ValidationError(
                {'name': "please enter a first name"})
        if len(self.user.last_name) == 0:
            raise ValidationError(
                {'name': "please enter a last name"})
        if len(self.dob) == 0:
            raise ValidationError(
                {'dob': "please enter a date of birth"})
        if  len(self.instruments) == 0:
            raise ValidationError(
                {'instruments': "Please enter an instrument"})
        if  len(self.bio) == 0:
            raise ValidationError(
                {'bio': "Please select a bio"})

def __str__(self):
            return self.user.username


