from django.urls import path, re_path, include

from . import views


create_urlpatterns = [
    re_path(r'^teacher/$', views.CreateTeacherView.as_view(), name='create teacher'),
    re_path(r'^student/$', views.CreateStudentView.as_view(), name='create student'),
    re_path(r'^school-class/$', views.CreateSchoolClassView.as_view(), name='create school class'),
]


urlpatterns = [
    re_path(r'^create/', include(create_urlpatterns)),
]