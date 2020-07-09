# Generated by Django 3.0.6 on 2020-07-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200708_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_status',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('headteacher', 'Headteacher')], default='student', max_length=11),
        ),
    ]
