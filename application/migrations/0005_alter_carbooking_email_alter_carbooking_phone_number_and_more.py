# Generated by Django 4.2.6 on 2023-10-18 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_carbooking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbooking',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='carbooking',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='ridebooking',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ridebooking',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]