# Generated by Django 4.1 on 2022-08-25 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
