# Generated by Django 4.1.1 on 2022-10-07 15:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_remove_inventory_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]