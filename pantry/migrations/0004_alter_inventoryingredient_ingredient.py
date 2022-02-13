# Generated by Django 4.0.1 on 2022-02-09 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0009_alter_ingredient_name'),
        ('pantry', '0003_rename_cook_user_pantry_cook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredient.ingredient'),
        ),
    ]
