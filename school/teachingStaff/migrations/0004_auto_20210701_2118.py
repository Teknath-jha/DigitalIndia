# Generated by Django 3.1.5 on 2021-07-01 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachingStaff', '0003_auto_20210701_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='jtd_sr',
            new_name='jtdsr',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='std_1',
            new_name='std1',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='std_10',
            new_name='std10',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='std_2',
            new_name='std2',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='std_3',
            new_name='std3',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='std_4',
            new_name='std4',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='std_5',
            new_name='std5',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='std_6',
            new_name='std6',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='std_7',
            new_name='std7',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='std_8',
            new_name='std8',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='std_9',
            new_name='std9',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='std_jr',
            new_name='stdjr',
        ),
    ]