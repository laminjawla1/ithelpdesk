# Generated by Django 4.1.1 on 2022-12-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0025_alter_feedback_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='time',
            field=models.TimeField(default='20:35:53'),
        ),
    ]
