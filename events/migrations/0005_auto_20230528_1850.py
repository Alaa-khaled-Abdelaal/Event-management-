# Generated by Django 2.2.28 on 2023-05-28 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]
