# Generated by Django 3.1.1 on 2020-09-22 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('createT', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_student',
            new_name='is_diorganotis',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_teacher',
            new_name='is_simmetexon',
        ),
    ]
