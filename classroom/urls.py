from django.urls import path
from .views import (CourseView,
CourseCreateView, HomeView,
course_single,)

from django.conf import settings
from django.conf.urls.static import static

app_name = "classroom"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('course/', CourseView.as_view(), name='course'),
    path('course-create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/course-view/', course_single, name='course-view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)