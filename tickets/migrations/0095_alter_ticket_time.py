# Generated by Django 4.1.1 on 2022-10-31 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0094_alter_ticket_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='10:49:55'),
        ),
    ]
