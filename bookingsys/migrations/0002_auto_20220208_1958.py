# Generated by Django 3.2 on 2022-02-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='tables',
        ),
        migrations.AddField(
            model_name='schedule',
            name='tables',
            field=models.ManyToManyField(blank=True, related_name='timeslot', to='bookingsys.Table'),
        ),
    ]
