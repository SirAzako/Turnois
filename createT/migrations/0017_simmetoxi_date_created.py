# Generated by Django 3.1.1 on 2020-09-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createT', '0016_auto_20200928_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='simmetoxi',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
