# Generated by Django 4.0.3 on 2022-04-07 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0018_remove_members_age_delete_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_age', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='members',
            name='age',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.age'),
        ),
    ]
