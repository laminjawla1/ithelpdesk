# Generated by Django 4.1.1 on 2022-12-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0016_alter_ticket_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='branch',
            field=models.CharField(choices=[], max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='12:52:17'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='zone',
            field=models.CharField(choices=[], max_length=100),
        ),
    ]
