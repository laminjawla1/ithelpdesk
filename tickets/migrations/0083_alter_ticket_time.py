# Generated by Django 4.1.1 on 2022-10-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0082_alter_ticket_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='11:15:24'),
        ),
    ]