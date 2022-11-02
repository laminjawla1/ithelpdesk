# Generated by Django 4.1.1 on 2022-11-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0110_alter_ticket_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pics/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='15:22:17'),
        ),
    ]