# Generated by Django 3.0.6 on 2020-07-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolclass',
            name='name',
            field=models.CharField(choices=[('1A', 'One A'), ('1B', 'One B'), ('1C', 'One C'), ('2A', 'Two A'), ('2B', 'Two B'), ('2C', 'Two C')], max_length=100, unique=True),
        ),
    ]