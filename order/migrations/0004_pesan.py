# Generated by Django 5.1.2 on 2024-12-18 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_kamar_alter_notlppel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesan',
            fields=[
                ('idPesan', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Pesan')),
                ('jmlhKamar', models.PositiveIntegerField(verbose_name='Jumlah Kamar')),
                ('idPel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.pelanggan', verbose_name='ID Pelanggan')),
            ],
            options={
                'verbose_name_plural': 'Data Pesan Hotel',
                'ordering': ['idPesan'],
            },
        ),
    ]
