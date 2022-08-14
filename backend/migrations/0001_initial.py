# Generated by Django 3.2.12 on 2022-08-14 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventDate',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=None)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dates_of_event', to='backend.event')),
            ],
            options={
                'db_table': 'event_dates',
            },
        ),
        migrations.CreateModel(
            name='EventVote',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vote_for_date', to='backend.eventdate')),
            ],
            options={
                'db_table': 'event_votes',
            },
        ),
    ]