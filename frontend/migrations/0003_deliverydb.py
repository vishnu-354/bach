# Generated by Django 4.1.3 on 2023-02-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_reviewdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliverydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Ph_no', models.IntegerField()),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('qty', models.IntegerField()),
                ('totalprice', models.IntegerField()),
            ],
        ),
    ]
