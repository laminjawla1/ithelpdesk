# Generated by Django 4.1.1 on 2022-10-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_alter_ticket_category_alter_ticket_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='16:37:27'),
        ),
    ]