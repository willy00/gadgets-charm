# Generated by Django 3.0 on 2019-07-26 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='id_name',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
