# Generated by Django 4.0.5 on 2022-06-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_delete_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
