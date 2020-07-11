from django.urls import path, re_path, include

from . import views


create_urlpatterns = [
    re_path(r'^teacher/$', views.CreateTeacherView.as_view(), name='create teacher'),
    re_path(r'^student/$', views.CreateStudentView.as_view(), name='create student'),
    re_path(r'^school-class/$', views.CreateSchoolClassView.as_view(), name='create school class'),
    re_path(r'^subject/$', views.CreateSubjectView.as_view(), name='create subject'),
    re_path(r'^grade/$', views.CreateGradeView.as_view(), name='create grade'),
]


modify_urlpatterns = [

]


urlpatterns = [
    re_path(r'^home/$', views.HomeView.as_view(), name='home'),
    re_path(r'^create/', include(create_urlpatterns)),
    re_path(r'^modify/', include(modify_urlpatterns)),
]