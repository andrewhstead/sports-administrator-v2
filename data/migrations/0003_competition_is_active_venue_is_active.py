# Generated by Django 4.1.3 on 2022-12-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_state_alter_competition_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
