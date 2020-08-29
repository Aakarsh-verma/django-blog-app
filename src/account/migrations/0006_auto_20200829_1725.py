# Generated by Django 3.1 on 2020-08-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_youtube_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='organization_name',
            field=models.CharField(default='Pillai', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='organization_place',
            field=models.CharField(default='New Panvel', max_length=200),
            preserve_default=False,
        ),
    ]