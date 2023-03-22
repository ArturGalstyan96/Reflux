from django.contrib import admin
from .models import (UserInfo, AboutMe, 
                     Content, Skill, 
                     Prof, Image, 
                     Work, Contact)
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(AboutMe)
admin.site.register(Skill)
admin.site.register(Prof)
admin.site.register(Image)
admin.site.register(Work)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'email']
