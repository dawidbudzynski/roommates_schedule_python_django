# Generated by Django 2.0.3 on 2018-04-01 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roommates_app', '0011_auto_20180331_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cleaning',
            old_name='week',
            new_name='index',
        ),
    ]