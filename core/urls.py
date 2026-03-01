from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from .views import (SubjectViewSet,CategoryViewSet,
                    AgeGroupViewSet,ScheduleViewSet,GradeViewSet,
                    ActivityViewSet,HomeworkViewSet,AnnouncementViewSet, RegisterUserViewSet,LoginUserView,StatusViewSet,LogoutUserView)


router = DefaultRouter()
router.register('status' ,StatusViewSet , basename='status')
router.register('register' ,RegisterUserViewSet , basename='register')
router.register('subjects' ,SubjectViewSet , basename='subjects')
router.register('grades' ,GradeViewSet , basename='grades')
router.register('categories' ,CategoryViewSet , basename='categories')
router.register('age-groups' ,AgeGroupViewSet , basename='age-groups')
router.register('schedules' ,ScheduleViewSet , basename='schedules')
router.register('activities' ,ActivityViewSet , basename='activities')
router.register('homeworks' ,HomeworkViewSet , basename='homeworks')
router.register('announcements' ,AnnouncementViewSet , basename='announcements')



urlpatterns = router.urls
urlpatterns += [
    path('login/' , LoginUserView.as_view()),
    path('logout/' , LogoutUserView.as_view())
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)