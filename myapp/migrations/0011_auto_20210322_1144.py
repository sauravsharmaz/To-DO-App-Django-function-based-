# Generated by Django 3.1.6 on 2021-03-22 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20210322_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(default='No image provided', upload_to='static/myapps/videos'),
        ),
    ]