# Generated by Django 4.1.1 on 2022-10-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_alter_ticket_date_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='category',
            field=models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware'), ('Liveware', 'Liveware'), ('Server', 'Server')], default=('Software', 'Software'), max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='cycle',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Open', 'Open'), ('Progress', 'Progress'), ('Closed', 'Closed')], default=('Pending', 'Pending'), max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Mid', 'Mid'), ('High', 'High'), ('Very High', 'Very High')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='16:29:44'),
        ),
    ]
