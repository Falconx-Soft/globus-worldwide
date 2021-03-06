# Generated by Django 4.0.2 on 2022-03-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_alter_ware_house_model_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ware_house_model',
            name='length',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ware_house_model',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ware_house_model',
            name='storage_space',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ware_house_model',
            name='weight',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ware_house_model',
            name='width',
            field=models.FloatField(null=True),
        ),
    ]
