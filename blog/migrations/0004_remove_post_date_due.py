# Generated by Django 3.0.4 on 2020-04-23 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200419_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_due',
        ),
    ]
