# Generated by Django 2.2.1 on 2019-06-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passHash', '0004_auto_20190609_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_url',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='passhash',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
