# Generated by Django 4.1.1 on 2022-10-07 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_inventory_category_alter_inventory_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='date',
        ),
    ]
