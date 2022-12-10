# Generated by Django 4.1.1 on 2022-11-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.TimeField(default='08:34:12')),
            ],
        ),
    ]
