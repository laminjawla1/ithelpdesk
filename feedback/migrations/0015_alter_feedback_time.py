# Generated by Django 4.1.1 on 2022-10-08 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0014_alter_feedback_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='time',
            field=models.TimeField(default='00:46:14'),
        ),
    ]
