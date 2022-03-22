from django.contrib import admin
from BandBrowser.models import Band, Post, UserProfile

class BandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Band,BandsAdmin)
admin.site.register(Post)
admin.site.register(UserProfile)
