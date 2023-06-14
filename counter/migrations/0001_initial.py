# Generated by Django 4.2.1 on 2023-06-13 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractComparisonResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('price', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='M2ComparisonResult',
            fields=[
                ('abstractcomparisonresult_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='counter.abstractcomparisonresult')),
                ('offer_id', models.PositiveBigIntegerField()),
                ('in_moderation', models.BooleanField(default=False)),
            ],
            bases=('counter.abstractcomparisonresult',),
        ),
        migrations.CreateModel(
            name='RMComparisonResult',
            fields=[
                ('abstractcomparisonresult_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='counter.abstractcomparisonresult')),
                ('offer_id', models.PositiveBigIntegerField()),
                ('sellable', models.BooleanField(default=True)),
            ],
            bases=('counter.abstractcomparisonresult',),
        ),
        migrations.CreateModel(
            name='ComparisonResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('UNMATCH', 'Не прошёл сравнение состояний'), ('MODERATION', 'Находится на модерации в М2'), ('SELLABILITY', 'sellable=false в базе RM')], max_length=256)),
                ('checked_at', models.DateTimeField(auto_now_add=True)),
                ('m2_result', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='counter.m2comparisonresult')),
                ('rm_result', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='counter.rmcomparisonresult')),
            ],
        ),
    ]