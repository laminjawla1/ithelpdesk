# Generated by Django 4.1.1 on 2022-10-06 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_remove_ticket_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Low'), ('2', 'Mid'), ('3', 'High'), ('4', 'Very High')], max_length=10),
        ),
    ]
