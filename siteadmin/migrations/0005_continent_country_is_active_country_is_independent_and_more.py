# Generated by Django 4.1.3 on 2022-12-08 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0004_user_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=5)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='country',
            name='is_independent',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='flag',
            field=models.ImageField(upload_to='images/countries'),
        ),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_continent', to='siteadmin.continent'),
        ),
    ]