# Generated by Django 4.1.1 on 2022-10-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0086_alter_feedback_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='time',
            field=models.TimeField(default='11:26:04'),
        ),
    ]
