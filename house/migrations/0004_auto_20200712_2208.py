# Generated by Django 3.0.8 on 2020-07-12 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_auto_20200712_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='bedroom_num',
            new_name='bedroom',
        ),
    ]