# Generated by Django 3.1 on 2020-09-11 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adpost',
            old_name='url',
            new_name='adlink',
        ),
    ]
