# Generated by Django 4.1.1 on 2022-10-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0029_specialization_remove_ticket_assigned_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='09:13:15'),
        ),
    ]
