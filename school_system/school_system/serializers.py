# external imports
from rest_framework import serializers

# internal imports
from .models import Teacher, Student, SchoolClass, User, Subject, Grade

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'is_active', 'user_status']

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    subject = serializers.StringRelatedField()

    class Meta:
        model = Teacher
        fields = '__all__'

class SchoolClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = SchoolClass
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    school_class = SchoolClassSerializer()

    class Meta:
        model = Student
        fields = ['user', 'school_class']

class GradeSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    student = StudentSerializer()
    subject = serializers.StringRelatedField()

    class Meta:
        model = Grade
        fields = '__all__'