# Generated by Django 4.1.1 on 2022-10-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0043_expert_address_expert_email_expert_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='21:11:43'),
        ),
    ]
