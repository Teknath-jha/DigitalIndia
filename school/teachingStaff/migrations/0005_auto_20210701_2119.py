# Generated by Django 3.1.5 on 2021-07-01 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachingStaff', '0004_auto_20210701_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='jtdsr',
            new_name='stdSr',
        ),
    ]
