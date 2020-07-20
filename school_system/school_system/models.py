# external imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.core.validators import MaxValueValidator, MinValueValidator

# internal imports
from user.models import User



@receiver(user_signed_up)
def after_user_signed_up(request, user, **kwargs):
    ''' executes when new user signed up '''

    # add new user to relevant group
    status = user.user_status
    group = Group.objects.get(name=status)
    user.groups.add(group)
    # print(pretty_request(request))
    # if status == 'teacher':


class SubjectsTypes(models.TextChoices):
    NOT_PROVIDED = 'NP', _('Not provided')
    MATH = 'MA', _('Math')
    ENGLISH = 'ENG', _('English')
    BIOLOGY = 'BIO', _('Biology')


class ClassesNames(models.TextChoices):
        # CLASSES_NAMES = (
        #     ('1A', '1A'),
        #     ('1B', '1B'),
        #     ('2A', '2A'),
        #     ('2B', '2B'),
        # )
        ONE_A = 'A', _('One A')
        ONE_B = '1B', _('One B')
        ONE_C = '1C', _('One C')
        TWO_A = '2A', _('Two A')
        TWO_B = '2B', _('Two B')
        TWO_C = '2C', _('Two C')

class Subject(models.Model):
    name = models.CharField(max_length=25, choices=SubjectsTypes.choices)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # subject = models.CharField(max_length=3, choices=SubjectsTypes.choices, default=SubjectsTypes.NOT_PROVIDED)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username

class SchoolClass(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, choices=ClassesNames.choices, unique=True, default="XXXXXX")

    class Meta:
        verbose_name_plural = 'SchoolClasses'

    def __str__(self):
        return self.name

    def get_class_students(self):
        return self.student_set.all()

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.user.username

class Grade(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    wage = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        ordering = ['-subject']
