from django.contrib import admin
from .models import User, Story, StoryCategory, ReadingList, Projects, Imp, Studio
from tinymce.widgets import TinyMCE
from django.db import models

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name", {'fields': ["name"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

class StoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name/Date", {'fields': ["name", "date"]}),
        ('Description',{'fields':['description']}),
        ("Content", {"fields": ["content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
class StoryCategoryAdmin(admin.ModelAdmin):
    
    formfield_overrides = {
    models.TextField: {'widget': TinyMCE()},
    }

class StoryAdmin(admin.ModelAdmin):
        formfield_overrides = {
    models.TextField: {'widget': TinyMCE()},
    }

class ImpAdmin(admin.ModelAdmin):
        formfield_overrides = {
    models.TextField: {'widget': TinyMCE()},
    }








# Register your models here.
admin.site.register(User)
admin.site.register(Story, StoryAdmin)
admin.site.register(StoryCategory, StoryCategoryAdmin)
admin.site.register(Imp, ImpAdmin)
admin.site.register(Projects)
admin.site.register(ReadingList)
admin.site.register(Studio)