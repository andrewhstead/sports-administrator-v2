# Generated by Django 4.1.3 on 2022-12-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0006_state_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='is_recognised',
            field=models.BooleanField(default=True),
        ),
    ]
