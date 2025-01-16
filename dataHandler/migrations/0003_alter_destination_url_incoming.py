# Generated by Django 4.0.1 on 2025-01-16 03:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dataHandler', '0002_remove_destination_id_destination_destination_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='url',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('incoming_id', models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('data', models.TextField()),
                ('destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomings', to='dataHandler.destination')),
            ],
        ),
    ]
