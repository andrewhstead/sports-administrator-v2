# Generated by Django 4.1.3 on 2022-12-04 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0001_initial'),
        ('siteadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_country', to='siteadmin.country'),
        ),
        migrations.AddField(
            model_name='competition',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_sport', to='siteadmin.sport'),
        ),
    ]
