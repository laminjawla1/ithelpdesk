# Generated by Django 4.1.1 on 2022-10-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0035_remove_expert_tasks_ticket_assigned_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='10:45:59'),
        ),
    ]
