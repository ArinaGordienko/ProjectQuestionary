# Generated by Django 2.1.3 on 2018-11-21 01:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinput',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
