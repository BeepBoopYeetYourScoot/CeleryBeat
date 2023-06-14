# Generated by Django 4.2.1 on 2023-06-13 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abstractcomparisonresult',
            name='name',
        ),
        migrations.RemoveField(
            model_name='m2comparisonresult',
            name='offer_id',
        ),
        migrations.RemoveField(
            model_name='rmcomparisonresult',
            name='offer_id',
        ),
        migrations.AddField(
            model_name='abstractcomparisonresult',
            name='offer_id',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rmcomparisonresult',
            name='price_count',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rmcomparisonresult',
            name='quantity_count',
            field=models.PositiveIntegerField(null=True),
        ),
    ]