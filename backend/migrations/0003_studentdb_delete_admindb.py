# Generated by Django 4.1.3 on 2023-01-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_admindb_city_remove_admindb_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='admindb',
        ),
    ]