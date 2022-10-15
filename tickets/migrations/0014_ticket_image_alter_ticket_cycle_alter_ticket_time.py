# Generated by Django 4.1.1 on 2022-10-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0013_alter_ticket_date_closed_alter_ticket_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='cycle',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Open', 'Open'), ('Progress', 'Progress'), ('Closed', 'Closed')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='20:38:53'),
        ),
    ]
