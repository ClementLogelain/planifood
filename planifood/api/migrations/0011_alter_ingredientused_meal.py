# Generated by Django 4.0.2 on 2022-02-26 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_ingredientused_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientused',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used', to='api.meal'),
        ),
    ]
