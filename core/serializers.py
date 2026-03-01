from typing import reveal_type
from rest_framework.validators import ValidationError
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import User ,Categorie,Schedule,Subject,AgeGroup,Announcement,Activitie,Grade,Homework,Status


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id' , 'name']

class RegisterUserSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='status.name',default='Pending')

    class Meta:
        model = User
        fields = ['id' ,
                  'email' ,
                  'password' ,
                  'is_staff' ,
                  'status' ,
                  'username',
                  'is_parent' ,
                  'phone_number' ,
                  'full_name',
                  'registration_form',
                  'is_staff','date_joined']

    def create(self, validated_data):
        password = validated_data.pop('password')
        status = validated_data.pop('status')
        pending = Status.objects.get(name = 'Pending')
        user = User.objects.create_user(status=pending ,password=password ,**validated_data)
        return user

class LoginUserSerializer(TokenObtainPairSerializer):

    username_field = 'email'

    def validate(self,attrs):

        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email , password=password)

        if not user:
            raise ValidationError("Invalid Details")
        data = super().validate({
            self.username_field : email,
            'password' :password
        })
        data['is_staff'] = self.user.is_staff
        data['status'] =self.user.status.name
        data['is_parent'] = self.user.is_parent

        return data




class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id' , 'name' , 'slug' , 'date_created']

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id' , 'grade' , 'slug' , 'date_created']

class HomeworkSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    grade = serializers.PrimaryKeyRelatedField(queryset=Grade.objects.all())

    subject_name = serializers.CharField(source='subject' , read_only=True)
    grade_name = serializers.CharField(source='grade', read_only=True)

    class Meta:
        model = Homework
        fields = ['id' , 'title' , 'subject' , 'grade' , 'due_date' , 'description', 'subject_name', 'grade_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id' , 'name' , 'slug' , 'date_created']

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id' , 'name' , 'slug' , 'date_created']

class AgeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGroup
        fields = ['id' , 'name' , 'slug' , 'date_created']



class ActivitySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Categorie.objects.all())
    schedule = serializers.PrimaryKeyRelatedField(queryset=Schedule.objects.all())
    age_group = serializers.PrimaryKeyRelatedField(queryset=AgeGroup.objects.all())

    category_name = serializers.CharField(source='category' , read_only=True)
    schedule_name = serializers.CharField(source='schedule', read_only=True)
    age_group_name = serializers.CharField(source='age_group', read_only=True)

    class Meta:
        model = Activitie
        fields = ['id' , 'title' , 'category' , 'schedule' , 'age_group' ,
                  'description', 'category_name', 'schedule_name' , 'age_group_name']

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id' , 'title' , 'description' , 'date_created' , 'date']