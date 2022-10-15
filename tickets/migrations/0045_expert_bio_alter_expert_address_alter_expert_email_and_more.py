# Generated by Django 4.1.1 on 2022-10-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0044_alter_ticket_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expert',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='expert',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='expert',
            name='level',
            field=models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Amateur', 'Amateur'), ('Intermediate', 'Intermediate'), ('Advance', 'Advance'), ('Pro', 'Pro')], default='Beginner', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='expert',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='expert',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='expert',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='expert',
            name='specialization',
            field=models.ManyToManyField(blank=True, to='tickets.specialization'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default='10:48:06'),
        ),
    ]
