# Generated by Django 3.2.7 on 2021-09-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20210921_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.IntegerField(default=1, help_text='duration of the quiz in minutes'),
            preserve_default=False,
        ),
    ]
