# Generated by Django 2.2.1 on 2019-05-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passHash', '0002_user_passhash'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]