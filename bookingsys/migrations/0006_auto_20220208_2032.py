# Generated by Django 3.2 on 2022-02-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0005_rename_table_bookingslot_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='TSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.TimeField(unique=True)),
                ('endTime', models.TimeField(unique=True)),
                ('closed', models.IntegerField(choices=[(0, 'Closed'), (1, 'Open')], default=0)),
            ],
            options={
                'ordering': ['-startTime'],
            },
        ),
        migrations.RemoveField(
            model_name='bookingslot',
            name='time',
        ),
        migrations.AlterField(
            model_name='bookingslot',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
