# Generated by Django 4.1.1 on 2022-10-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0066_expert_social_alter_ticket_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expert',
            name='social',
        ),
        migrations.AddField(
            model_name='expert',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='16:57:06'),
        ),
    ]
