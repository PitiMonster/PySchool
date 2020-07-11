# external imports
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# internal imports
from ..models import Teacher, Student, SchoolClass, User, Subject, Grade
from ..decorators import allowed_users


# class ModifyTeacherView(APIView):
    
#     @allowed_users(allowed_roles=['headteacher'])
#     def post(self, request):
