# Generated by Django 4.1.1 on 2022-11-01 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0116_alter_feedback_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='time',
            field=models.TimeField(default='15:54:27'),
        ),
    ]
