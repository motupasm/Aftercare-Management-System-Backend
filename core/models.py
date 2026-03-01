from django.db import models
from django.contrib.auth.models import AbstractUser


class Status(models.Model):
    STATUS_CHOICES = [('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')]
    name = models.CharField(max_length=255, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class User(AbstractUser):

    email = models.CharField(max_length=255 , unique=True)
    username = models.CharField(max_length=255 , blank=True , null=True)
    full_name = models.CharField(max_length=255, blank=True ,null=True)
    phone_number = models.CharField(max_length=255)
    status = models.ForeignKey(Status , on_delete=models.DO_NOTHING , related_name='user' , default=1 )
    is_parent = models.BooleanField(default=False)
    registration_form = models.FileField(upload_to='registration_forms/' , null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Subject(models.Model):

    SUBJECT_CHOICES = [('Mathematics' , 'Mathematics') , ('Physics' , 'Physics') , ('Arts' , 'Arts'),('History' , 'History')]

    name = models.CharField(max_length=255 , choices=SUBJECT_CHOICES)
    slug = models.SlugField(unique=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Grade(models.Model):

    GRADE_CHOICES = [('Grade 1' , 'Grade 1') , ('Grade 2' , 'Grade 2'),('Grade 3' , 'Grade 3') , ('Grade 4' , 'Grade 4')]

    grade = models.CharField(max_length=255, choices=GRADE_CHOICES)
    slug = models.SlugField(unique=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.grade

class Homework(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE , related_name='homework')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='homework')
    due_date = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Categorie(models.Model):

    CATEGORY_CHOICES = [('Creative' , 'Creative') , ('Stem' , 'Stem'),('Physical' , 'Physical') , ('Academic' , 'Academic')]

    name = models.CharField(max_length=255 , choices=CATEGORY_CHOICES)
    slug = models.SlugField(unique=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):

    SCHEDULE_CHOICES = [('daily' , 'Daily') , ('Mon & Wed' , 'Mon & Wed'), ('Thu & Fri' , 'Thu & Fri')]

    name = models.CharField(max_length=255, choices=SCHEDULE_CHOICES)
    slug = models.SlugField(unique=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class AgeGroup(models.Model):

    AGE_GROUP_CHOICES = [('Group K' , 'Group K') , ('Group K-2' , 'Group K-2'),('Group K-3' , 'Group K-3'),('Group K-4' , 'Group K-4')]

    name = models.CharField(max_length=255, choices=AGE_GROUP_CHOICES)
    slug = models.SlugField(unique=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activitie(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Categorie , on_delete=models.CASCADE , related_name='activity')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='activity')
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE, related_name='activity')
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title