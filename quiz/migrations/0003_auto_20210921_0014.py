# Generated by Django 3.2.7 on 2021-09-20 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('quiz', '0002_auto_20210920_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='Level',
            new_name='level',
        ),
        migrations.AlterField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student'),
        ),
    ]