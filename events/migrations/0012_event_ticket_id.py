# Generated by Django 2.2.28 on 2023-05-31 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_remove_event_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ticket_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Ticket'),
        ),
    ]
