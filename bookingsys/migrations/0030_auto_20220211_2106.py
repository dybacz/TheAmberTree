# Generated by Django 3.2 on 2022-02-11 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0029_alter_bookingslot_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timeslot',
            options={'ordering': ['startTime']},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_id',
        ),
    ]