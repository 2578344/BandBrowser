from django.db import models
from django.template.defaultfilters import slugify
from tabnanny import verbose

class Band(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    genres = models.CharField(max_length=32)
    commitment = models.CharField(max_length=32)
    location = models.CharField(max_length=128)
    dateCreated = models.DateField(max_length=128)
    numberOfPostsActive = models.IntegerField(default=0)
    numberOfCurrentMembers = models.IntegerField(default=0)
    numberOfPotentialMembers = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Band, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Bands'

    def __str__(self):
        return self.name

class Post(models.Model):
    TITLE_MAX_LENGTH=128
    # band = models.ForeignKey(Band, on_delete=models.CASCADE)
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