# Generated by Django 4.1.1 on 2022-12-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0021_alter_ticket_time_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='17:25:00'),
        ),
    ]
