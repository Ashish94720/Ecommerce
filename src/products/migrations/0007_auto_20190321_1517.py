# Generated by Django 2.1.7 on 2019-03-21 09:47

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190321_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, height_field='100', null=True, upload_to=products.models.upload_image_path, width_field='100'),
        ),
    ]
