# Generated by Django 5.0.6 on 2024-05-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPG_FUNCTIONS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamepost',
            name='header',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
