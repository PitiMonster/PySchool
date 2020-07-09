# external imports
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# internal imports
from .models import Teacher, Student, SchoolClass, User, Subject, Grade
from .decorators import allowed_users


class CreateTeacherView(APIView):

    @allowed_users(allowed_roles=['headteacher'])
    def post(self, request):
        new_teacher_email = request.data['new_teacher_email']
        try:
            new_teacher = User.objects.get(email=new_teacher_email)
        except User.DoesNotExist:
            return Response({'content': 'Teacher with this email does not exist!'})

        # check if given user is allowed to be a teacher
        if new_teacher.user_status != 'teacher':
            return Response({'content': 'That user has not teacher status!'})
        
        subject = request.data['subject']

        new_teacher = Teacher(user=new_teacher, subject=subject)
        new_teacher.save()

        return Response({'content': True})

class CreateStudentView(APIView):

    @allowed_users(allowed_roles=['heeadteacher'])
    def post(self, request):
        new_student_email = request.data['new_student_email']

        try:
            new_student = User.objects.get(email=new_student_email)
        except User.DoesNotExist:
            return Response({'content': 'Student with this email does not exist!'})

        if new_student.user_status != 'student':
            return Response({'content': 'That user has not student status!'})

        school_class_name = request.data['school_class_name']
        
        try:
            school_class = SchoolClass.objects.get(name=school_class_name)
        except SchoolClass.DoesNotExist:
            return Response({'content': 'School class with tihs name does not exist!'})

        new_student = Student(user=new_student, school_class=school_class)
        new_student.save()

        return Response({'content': True})

class CreateSchoolClassView(APIView):

    @allowed_users(allowed_roles=['headteacher'])
    def post(self, request):
        class_teacher_email = request.data['class_teacher_email']

        try:
            teacher = User.objects.get(email=class_teacher_email)
        except User.DoesNotExist:
            return Response({'content': 'Teacher with this email does not exist!'})

        try:
            class_teacher = Teacher.objects.get(user=teacher)
        except Teacher.DoesNotExist:
            return Response({'content': 'Teacher with this email does not exist!'})

        teacher_classes = class_teacher.schoolclass_set.all()
        if teacher_classes:
            return Response({'content': 'That teacher has class already!'})

        school_class_name = request.data['school_class_name']

        new_school_class = SchoolClass(teacher=class_teacher, name=school_class_name)
        new_school_class.save()

        return Response({'content': True})

class CreateSubjectView(APIView):

    @allowed_users(allowed_roles=['headteacher'])
    def post(self, request):
        subject_name = request.data['subject_name']

        try:
            new_subject = Subject(name=subject_name)
            new_subject.save()
            return Response({'content': True})
        except:
            return Response({'content': 'Cannot create such subject!'})


class CreateGradeView(APIView):
    
    @allowed_users(allowed_roles=['headteacher', 'teacher'])
    def post(self, request):

        teacher_pk = request.data['teacher_pk']
        try:
            teacher = Teacher.objects.get(pk=int(teacher_pk))
        except Teacher.DoesNotExist:
            return Response({'content': 'Teacher with this pk does not exist!'})

        student_pk = request.data['student_pk']
        try:
            student = Student.objects.get(pk=int(student_pk))
        except Student.DoesNotExist:
            return Response({'content': 'Student with this pk does not exist!'})

        subject_name = request.data['subject_name']
        try:
            subject = Subject.objects.get(name=subject_name)
        except Teacher.DoesNotExist:
            return Response({'content': 'Subject with this name does not exist!'})

        wage = request.data['wage']

        try:
            new_grade = Grade(teacher=teacher, student=student, subject=subject, wage=int(wage))
            new_grade.save()
            return Response({'content': True})
        except:
            return Response({'content': 'Unexpected error occured. Try again!'})