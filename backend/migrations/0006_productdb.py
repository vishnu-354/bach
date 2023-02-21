# Generated by Django 4.1.3 on 2023-01-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_instrumentdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.CharField(max_length=100)),
                ('Product', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
