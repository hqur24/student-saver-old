# Generated by Django 3.0.4 on 2020-04-23 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_date_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_due',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
