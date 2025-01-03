# Generated by Django 2.2.28 on 2023-05-31 11:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_delete_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date (Morocco)')),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated Date (Morocco)')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='events.Event')),
            ],
        ),
    ]
