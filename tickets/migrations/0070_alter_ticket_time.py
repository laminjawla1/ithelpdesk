# Generated by Django 4.1.1 on 2022-10-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0069_alter_ticket_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='09:47:38'),
        ),
    ]
