# Generated by Django 4.1.1 on 2022-11-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_alter_ticket_time_alter_ticket_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='14:33:38'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='zone',
            field=models.CharField(choices=[('Basse', 'Basse'), ('Westfield', 'Westfield'), ('Tabokoto', 'Tabokoto'), ('Bansang', 'Bansang'), ('Brusibi', 'Brusibi'), ('Tippagarage', 'Tippagarage'), ('Soma', 'Soma'), ('Brikama', 'Brikama')], max_length=100),
        ),
    ]
