# Generated by Django 4.1.1 on 2022-11-01 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0106_alter_feedback_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='time',
            field=models.TimeField(default='13:03:17'),
        ),
    ]
