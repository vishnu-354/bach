# Generated by Django 4.1.3 on 2023-02-15 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_deliverydb'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverydb',
            name='Products',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
