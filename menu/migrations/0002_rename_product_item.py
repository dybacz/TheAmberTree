# Generated by Django 3.2 on 2022-07-04 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
    ]