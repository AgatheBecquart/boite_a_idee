from django.contrib import admin
from .models import Idea, Like, Dislike

admin.site.register(Idea)
admin.site.register(Like)
admin.site.register(Dislike)
