# Generated by Django 2.2 on 2021-04-01 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_carts_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='shop_id',
            field=models.IntegerField(null=True),
        ),
    ]
