# Generated by Django 4.1.1 on 2022-10-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0090_alter_ticket_branch_alter_ticket_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='11:32:43'),
        ),
    ]
