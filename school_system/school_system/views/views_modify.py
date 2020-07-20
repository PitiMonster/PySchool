# external imports
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, HttpResponseNotFound

# internal imports
from ..models import Teacher, Student, SchoolClass, User, Subject, Grade
from ..decorators import allowed_users
from ..utils import get_objects_by_id


class ModifyTeacherView(APIView):
    
    @allowed_users(allowed_roles=['headteacher'])
    def post(self, request):
        '''
        provide:
        - teacher_id,
        - subject_id
        '''
        teacher, new_subject = get_objects_by_id(['teacher_id', 'subject_id'], request)

        if not teacher:
            return HttpResponseNotFound('Wrong data provided!')

        try:
            teacher.subject = new_subject
            teacher.save()
            return Response({'content': True})
        except:
            return Response({'content': 'Unexpected error occurred. Try again!'})

class ModifySchoolClassView(APIView):

    @allowed_users(allowed_roles=['headteacher'])
    def post(self, request):
        '''
        provide:
        - school_class_id,
        - teacher_id,
        - new_name
        '''
        school_class, new_teacher = get_objects_by_id(['school_class_id', 'teacher_id'], request)

        if not school_class:
            return HttpResponseNotFound('Wrong data provided!')

        new_name = request.data['new_name']

        try:
            school_class.teacher = new_teacher
            school_class.name = new_name
            school_class.save()
            return Response({'content': True})
        except:
            return Response({'content': 'Unexpected error occurred. Try again!'})

class ModifyStudentView(APIView):

    @allowed_users(allowed_roles=['headteacher'])
    def post(self, request):
        '''
        provide:
        - student_id,
        - new_class_id
        '''
        student, new_class = get_objects_by_id(['student_id', 'new_class_id'], request)

        if not student:
            return HttpResponseNotFound('Wrong data provided!')

        try:
            student.school_class = new_class
            student.save()
            return Response({'content': True})
        except:
            return Response({'content': 'Unexpected error occurred. Try again!'})

class ModifyGradeView(APIView):

    @allowed_users(allowed_roles=['headteacher', 'teacher'])
    def post(self, request):
        '''
        provide:
        - grade_id,
        - teacher_id,
        - subject_id,
        - grade_value,
        - wage
        '''

        grade, teacher, subject = get_objects_by_id(['grade_id', 'teacher_id', 'subject_id'], request)

        if not grade:
            return HttpResponseNotFound('Wrong data provided!')

        curr_user = request.user

        # only headteacher or teacher who gave a grade can modify it
        if curr_user.user_status != 'headteacher':
            if grade.teacher != curr_user:
                return Response({'content': 'You are not granted to modify this grade!'})

        new_grade_value = int(request.data['grade_value'])
        new_wage = int(request.data['wage'])

        try:
            grade.grade = new_grade_value
            grade.wage = new_wage
            grade.teacher = teacher
            grade.subject = subject
            grade.save()
            return Response({'content': True})
        except:
            return Response({'content': 'Unexpected error occurred. Try again!'})