# Generated by Django 2.2 on 2021-03-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('time_created', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'customer_carts',
            },
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('time_created', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'customer_favorites',
            },
        ),
    ]
