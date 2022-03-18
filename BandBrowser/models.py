from django.db import models
from django.template.defaultfilters import slugify
from tabnanny import verbose
from django.contrib.auth.models import User

class Post(models.Model):
    TITLE_MAX_LENGTH=128
    postID = models.CharField(max_length=11, unique=True)
    #band = models.ForeignKey(Band, on_delete=models.CASCADE,default="")
    #user = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    description = models.CharField(max_length=1000)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    publishDate = models.DateField(max_length=128)
    expireDate = models.DateField()
    experienceRequired = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    genre = models.CharField(max_length=32)
    commitment = models.CharField(max_length=32)


    def __str__(self):
        return self.title


class Band(models.Model):
    NAME_MAX_LENGTH = 128
    post = models.ManyToManyField(Post)
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    genres = models.CharField(max_length=32)
    commitment = models.CharField(max_length=32)
    location = models.CharField(max_length=128)
    dateCreated = models.DateField(max_length=128)
    numberOfPostsActive = models.IntegerField(default=0)
    numberOfCurrentMembers = models.IntegerField(default=0)
    numberOfPotentialMembers = models.IntegerField(default=0)
    userProfile = models.ManyToManyField(User)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Band, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Bands'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    band = models.ManyToManyField(Band)
    post = models.ManyToManyField(Post)
    NAME_MAX_LENGTH=128
    userID = models.CharField(max_length=10, unique=True)
    firstName = models.CharField(max_length=NAME_MAX_LENGTH)
    lastName = models.CharField(max_length=NAME_MAX_LENGTH)
    email = models.CharField(max_length=100,unique=True)
    dob = models.DateField()
    instruments = models.TextField(null=True)
    linkedAccounts = models.TextField(null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(upload_to='profile_images', blank=True)
    numberOfBands = models.IntegerField(default=0)
    numberOfPostsActive = models.IntegerField(default=0)

    def __str__(self):
            return self.user.username


