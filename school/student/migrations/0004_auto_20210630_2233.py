# Generated by Django 3.1.5 on 2021-06-30 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_s_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='s_password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='s_name',
            new_name='username',
        ),
    ]