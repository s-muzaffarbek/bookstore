# Generated by Django 4.0.5 on 2022-06-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='qty',
            field=models.IntegerField(),
        ),
    ]