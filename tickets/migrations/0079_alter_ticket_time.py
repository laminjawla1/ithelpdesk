# Generated by Django 4.1.1 on 2022-10-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0078_alter_ticket_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='16:47:57'),
        ),
    ]
