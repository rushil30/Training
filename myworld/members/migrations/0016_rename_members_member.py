# Generated by Django 4.0.3 on 2022-04-07 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_alter_members_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]
