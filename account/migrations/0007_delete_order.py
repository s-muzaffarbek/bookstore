# Generated by Django 4.0.5 on 2022-07-29 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_delete_basket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
