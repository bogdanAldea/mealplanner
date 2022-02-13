# Generated by Django 4.0.1 on 2022-02-08 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0004_rename_cook_user_market_cook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pantry', to='ingredient.market'),
        ),
    ]