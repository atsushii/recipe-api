# Generated by Django 2.1.15 on 2021-01-26 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_ingredients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
    ]
