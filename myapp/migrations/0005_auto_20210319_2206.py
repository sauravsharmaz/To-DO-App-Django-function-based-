# Generated by Django 3.1.6 on 2021-03-19 16:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210319_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
