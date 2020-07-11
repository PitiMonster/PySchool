# Generated by Django 3.0.6 on 2020-07-11 08:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wage', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
            ],
            options={
                'ordering': ['-subject'],
            },
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A', 'One A'), ('1B', 'One B'), ('1C', 'One C'), ('2A', 'Two A'), ('2B', 'Two B'), ('2C', 'Two C')], default='XXXXXX', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'SchoolClasses',
            },
        ),
    ]
