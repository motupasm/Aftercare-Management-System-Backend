from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import (StatusSerializer,RegisterUserSerializer,LoginUserSerializer,
                          SubjectSerializer,ScheduleSerializer,
                          ActivitySerializer,GradeSerializer,CategorySerializer,HomeworkSerializer , AgeGroupSerializer ,AnnouncementSerializer)
from .models import User ,Categorie,Schedule,Subject,AgeGroup,Announcement,Activitie,Grade,Homework,Status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.decorators import action

class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class LoginUserView(TokenObtainPairView):
    serializer_class = LoginUserSerializer

class LogoutUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response('Logged out')


class RegisterUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    @action(detail=True , methods = ['patch'])
    def approve(self,request,pk=None):
        user = self.get_object()
        approved_status = Status.objects.get(name='Approved')
        user.status = approved_status
        user.save()

        message = (f'Hello {user.full_name},\n\nGreat news! Your account has been successfully approved.'
                   f'\n\nYou can now log in and access your dashboard.'
                   f'\n\nIf you experience any issues, please contact support.\n\nThank you for joining us.')


        send_mail(subject='Your Account Has Been Approved' ,
                  message=message ,
                  from_email=settings.EMAIL_HOST_USER,recipient_list=[user.email] , fail_silently=False)

        return Response({'message':'User approved'})

    @action(detail=True, methods=['patch'])
    def reject(self, request, pk=None):
        user = self.get_object()
        Rejected_status = Status.objects.get(name='Rejected')
        user.status = Rejected_status
        user.save()
        send_mail(subject='Account Rejection',
                  message='We regret to inform you that your account was not approved at this time.',
                  from_email=settings.EMAIL_HOST_USER, recipient_list=[user.email], fail_silently=False)
        return Response({'message': 'User Rejected'})


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class HomeworkViewSet(ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer

class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class AgeGroupViewSet(ModelViewSet):
    queryset = AgeGroup.objects.all()
    serializer_class = AgeGroupSerializer

class ActivityViewSet(ModelViewSet):
    queryset = Activitie.objects.all()
    serializer_class = ActivitySerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
