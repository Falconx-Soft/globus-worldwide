# Generated by Django 4.0.2 on 2022-03-09 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ware_house_model',
            name='warehouse',
            field=models.CharField(default='', max_length=20),
        ),
    ]