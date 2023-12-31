# Generated by Django 4.2.1 on 2023-06-13 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'managed': False, 'ordering': ['scallium_id']},
        ),
        migrations.AlterModelOptions(
            name='productoffer',
            options={'managed': False, 'ordering': ['scallium_id']},
        ),
        migrations.AlterModelOptions(
            name='productofferavailabilities',
            options={'default_related_name': 'availabilities', 'managed': False},
        ),
        migrations.AlterModelOptions(
            name='productofferprice',
            options={'default_related_name': 'prices', 'managed': False},
        ),
        migrations.AlterModelOptions(
            name='productofferquantities',
            options={'default_related_name': 'quantities', 'managed': False},
        ),
    ]
