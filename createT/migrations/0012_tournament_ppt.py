# Generated by Django 3.1.1 on 2020-09-26 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createT', '0011_auto_20200926_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='PpT',
            field=models.FloatField(null=True),
        ),
    ]
