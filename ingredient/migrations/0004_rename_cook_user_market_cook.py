# Generated by Django 4.0.1 on 2022-02-08 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0003_ingredient_market'),
    ]

    operations = [
        migrations.RenameField(
            model_name='market',
            old_name='cook_user',
            new_name='cook',
        ),
    ]