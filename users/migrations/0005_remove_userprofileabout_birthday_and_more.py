# Generated by Django 4.2.6 on 2023-10-18 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userprofileabout_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileabout',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='userprofileabout',
            name='relationship_status',
        ),
    ]
