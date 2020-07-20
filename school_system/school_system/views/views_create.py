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


class CreateTeacherView(APIView):

    @allowed_users(allowed_roles=['headteacher'])
    def post(self, request):
        '''
        provide:
        - user_id,
        - subject_id
        '''
        new_teacher, subject = get_objects_by_id(['user_id', 'subject_id'], request)

        # check if get_objects_by_id has succeed
        if not new_teacher:
            return HttpResponseNotFound('Wrong data provided!')
 
        # check if provided user has teacher status
        if new_teacher.user_status != 'teacher':
            return Response({'content': 'That user has not teacher status!'})

        try:
            new_teacher = Teacher(user=new_teacher, subject=subject)
            new_teacher.save()
            return Response({'content': True})
        except:
            return Response({'content': 'Unexpected error occurred. Try again!'})
            
class CreateStudentView(APIView):

    @allowed_users(allowed_roles=['headteacher'])
    def post(self, request):
        '''
        provide:
        - user_id,
        - school_class_id
        '''
        new_student, school_class = get_objects_by_id(['user_id', 'school_class_id'], request)

        # check if get_objects_by_id has succeed
        if not new_student:
            return HttpResponseNotFound('Wrong data provided!')

        # check if provided user has student status
        if new_student.user_status != 'student':
            return Response({'content': 'That user has not student status!'})

        try:
            new_student = Student(user=new_student, school_class=school_class)
            new_student.save()
            return Response({'content': True})
        except:
            return Response({'content': 'Unexpected error occurred. Try again!'})

class CreateSchoolClassView(APIView):

    @allowed_users(allowed_roles=['headteacher'])
    def post(self, request):
        '''
        provide:
        - class_teacher_id,
        - school_class_id
        '''
        class_teacher, school_class_name = get_objects_by_id(['class_teacher_id', 'school_class_id'], request)

        if not class_teacher:
            return HttpResponseNotFound('Wrong data provided!')

        # check if teacher has not class already
        teacher_classes = class_teacher.schoolclass_set.all()
        if teacher_classes:
            return Response({'content': 'That teacher has class already!'})


        try:
            new_school_class = SchoolClass(teacher=class_teacher, name=school_class_name)
            new_school_class.save()
            return Response({'content': True})
        except:
            return Response({'content': 'Unexpected error occurred. Try again!'})

class CreateSubjectView(APIView):

    @allowed_users(allowed_roles=['headteacher'])
    def post(self, request):
        '''
        provide:
        - subject_name
        '''
        subject_name = request.data['subject_name']

        try:
            new_subject = Subject(name=subject_name)
            new_subject.save()
            return Response({'content': True})
        except:
            return Response({'content': 'Unexpected error occurred. Try again!'})


class CreateGradeView(APIView):
    
    @allowed_users(allowed_roles=['headteacher', 'teacher'])
    def post(self, request):
        '''
        provide:
        - teacher_id,
        - student_id,
        - subject_id,
        - wage,
        - grade
        '''
        teacher, student, subject = get_objects_by_id(['teacher_id', 'student_id', 'subject_id'], request)

        if not teacher:
            return HttpResponseNotFound('Wrong data provided!')

        wage = request.data['wage']
        grade = request.data['grade']

        try:
            new_grade = Grade(teacher=teacher, student=student, subject=subject, wage=int(wage), grade=int(grade))
            new_grade.save()
            return Response({'content': True})
        except:
            return Response({'content': 'Unexpected error occurred. Try again!'})