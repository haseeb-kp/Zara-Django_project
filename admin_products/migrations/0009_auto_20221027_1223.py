# Generated by Django 3.2.16 on 2022-10-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_products', '0008_products_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/2'),
        ),
    ]
