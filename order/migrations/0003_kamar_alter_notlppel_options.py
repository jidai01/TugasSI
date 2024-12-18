# Generated by Django 5.1.2 on 2024-12-18 10:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_notlppel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kamar',
            fields=[
                ('idKamar', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='ID Kamar')),
                ('tipe', models.CharField(max_length=50, verbose_name='Tipe')),
                ('kapasitas', models.PositiveIntegerField(verbose_name='Kapasitas')),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Harga')),
            ],
            options={
                'verbose_name_plural': 'Data Kamar',
                'ordering': ['idKamar'],
            },
        ),
        migrations.AlterModelOptions(
            name='notlppel',
            options={'ordering': ['idNoTlpPel'], 'verbose_name_plural': 'Data Nomor Pelanggan'},
        ),
    ]
