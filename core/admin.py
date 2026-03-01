from django.contrib import admin
from .models import User ,Categorie,Schedule,Subject,AgeGroup,Announcement,Activitie,Grade,Homework,Status

admin.site.register(User)
admin.site.register(Categorie)
admin.site.register(Schedule)
admin.site.register(Subject)
admin.site.register(Activitie)
admin.site.register(Announcement)
admin.site.register(AgeGroup)
admin.site.register(Grade)
admin.site.register(Homework)
admin.site.register(Status)

