# Generated by Django 4.1.1 on 2022-10-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0027_alter_ticket_assigned_to_alter_ticket_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='07:41:46'),
        ),
    ]