# Generated by Django 5.1.4 on 2025-02-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]
