# Generated by Django 4.1.1 on 2022-11-01 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0097_ticket_submitter_name_alter_ticket_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='09:35:43'),
        ),
    ]
