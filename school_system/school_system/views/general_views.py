# external imports
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# internal imports
from ..models import Teacher, Student, SchoolClass, User, Subject, Grade
from ..decorators import allowed_users
from .. import serializers

class HomeView(APIView):
    permission_classes=[IsAuthenticated, ]

    def get(self, request):
        user = request.user

        response = {}

        if user.user_status == 'student':
            student = Student.objects.get(user=user)
            response['student'] = serializers.StudentSerializer(student).data
        elif user.user_status == 'teacher':
            teacher = Teacher.objects.get(user=user)
            response['teacher'] = serializers.TeacherSerializer(teacher).data
        else:
            return Response({'content': False})

        return Response({'content': response})    

