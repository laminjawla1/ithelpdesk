# Generated by Django 4.1.1 on 2022-10-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_alter_feedback_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={},
        ),
        migrations.AlterField(
            model_name='feedback',
            name='time',
            field=models.TimeField(default='16:37:27'),
        ),
    ]
