# Generated by Django 5.0.4 on 2024-06-22 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('granja', '0005_alter_produccion_cantidad_leche_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='edad_categoria',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
