# Generated by Django 4.1.1 on 2022-10-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0091_alter_ticket_phone_alter_ticket_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='09:34:13'),
        ),
    ]