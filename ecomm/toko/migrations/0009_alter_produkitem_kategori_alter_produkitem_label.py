# Generated by Django 4.2 on 2023-06-08 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0008_alter_alamatpengiriman_options_payment_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkitem',
            name='kategori',
            field=models.CharField(choices=[('A', 'Acne'), ('N', 'Normal'), ('S', 'Sensitive')], max_length=2),
        ),
        migrations.AlterField(
            model_name='produkitem',
            name='label',
            field=models.CharField(choices=[('NEW', 'new'), ('SALE', 'sale'), ('BEST', 'best')], max_length=4),
        ),
    ]
