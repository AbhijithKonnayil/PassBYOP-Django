# Generated by Django 2.2.1 on 2019-06-12 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passHash', '0006_auto_20190612_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='user',
            name='x0',
        ),
        migrations.RemoveField(
            model_name='user',
            name='x1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='x2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='x3',
        ),
        migrations.RemoveField(
            model_name='user',
            name='y0',
        ),
        migrations.RemoveField(
            model_name='user',
            name='y1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='y2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='y3',
        ),
    ]