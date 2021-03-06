# Generated by Django 3.1.1 on 2020-09-28 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('createT', '0014_tournament_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simmetoxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament', models.ManyToManyField(to='createT.Tournament')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
