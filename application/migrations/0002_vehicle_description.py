# Generated by Django 4.2.6 on 2023-10-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='description',
            field=models.TextField(default='Describe the car'),
        ),
    ]
