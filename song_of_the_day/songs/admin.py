from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib.auth.models import User, Group

class ProfileInline(admin.StackedInline):
    model = Profile

# class UserAdmin(admin.ModelAdmin):
#     model = User
#     fields = ["username"]
#     inlines = [ProfileInline]



# admin.site.unregister(User)
# admin.site.register(User)
admin.site.unregister(Group)
# # Remove: admin.site.register(Profile)