# Generated by Django 3.0.6 on 2020-07-09 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_system', '0002_auto_20200707_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolclass',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='school_class',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_system.SchoolClass'),
        ),
        migrations.AlterField(
            model_name='schoolclass',
            name='name',
            field=models.CharField(default='XXXXXX', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(choices=[('NP', 'Not provided'), ('MA', 'Math'), ('ENG', 'English'), ('BIO', 'Biology')], default='NP', max_length=3),
        ),
    ]